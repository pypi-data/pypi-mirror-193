"""
QQQR event system.
"""

import asyncio
from collections import defaultdict
from functools import wraps
from itertools import chain
from typing import (
    Any,
    Awaitable,
    Callable,
    Coroutine,
    Dict,
    Generic,
    List,
    Optional,
    Set,
    Tuple,
    Type,
    TypeVar,
    Union,
)

from typing_extensions import ParamSpec, final

from qqqr.exception import HookError

T = TypeVar("T")
P = ParamSpec("P")


class Event(Generic[T]):
    """Base class for event system.

    .. code-block:: python
        :linenos:
        :caption: my_events.py

        class Event1(Event):
            async def database_query(self, pid: int) -> str:
                pass

    .. code-block:: python
        :linenos:
        :caption: my_hooks.py

        from typing import TYPE_CHECKING

        if TYPE_CHECKING:
            from app import AppClass    # to avoid circular import

        class Event1Hook(Event1["AppClass"]):
            async def database_query(self, pid: int) -> str:
                return await self.scope.db.query(pid) or ""   # typing of scope is ok

    .. code-block:: python
        :linenos:
        :caption: service.py

        from my_event import Event1

        class Service(Emittable[Event1]):
            async def run(self):
                ...
                name = await self.hook.database_query(pid)
                ...

    .. code-block:: python
        :linenos:
        :caption: app.py

        from my_hooks import Event1Hook
        from service import Service

        class AppClass:
            db: Database

            def __init__(self):
                self.event1_hook = Event1Hook()
                self.event1_hook.link_to_scope(self)
                self.service = Service()
                self.service.register_hook(self.event1_hook)
    """

    scope: T
    """Access to a larger scope. This may allow hooks to achieve more functions.

    .. warning:: Can only be access after calling `link_to_scope`."""

    def link_to_scope(self, scope: T):
        """Set the :obj:`scope`."""
        self.scope = scope


Evt = TypeVar("Evt", bound=Event)


class NullEvent(Event):
    """For debugging"""

    __slots__ = ()

    def __getattribute__(self, __name: str):
        try:
            return super().__getattribute__(__name)
        except AttributeError:
            raise AssertionError("call `o.register_hook` before accessing `o.hook`")

    def __repr__(self) -> str:
        return "NullEvent()"


class Tasksets:
    """An object has some event to trigger."""

    _tasks: Dict[str, Set[asyncio.Task]]

    def __init__(self) -> None:
        self._tasks = defaultdict(set)

    def add_hook_ref(self, hook_cls, coro):
        # type: (str, Coroutine[Any, Any, T]) -> asyncio.Task[T]
        # NOTE: asyncio.Task becomes generic since py39
        task = asyncio.create_task(coro)
        self._tasks[hook_cls].add(task)
        task.add_done_callback(lambda t: self._tasks[hook_cls].remove(t))
        return task

    @final
    async def wait(
        self,
        *hook_cls: str,
        timeout: Optional[float] = None,
    ) -> Tuple[Set[asyncio.Task], Set[asyncio.Task]]:
        """Wait for all task in the specific task set(s).

        :param timeout: timeout, defaults to None
        :type timeout: float, optional
        :return: done, pending

        .. note::
            If `timeout` is None, this method will loop until all tasks in the set(s) are done.
            That means if other tasks are added during awaiting, the added task will be waited as well.

        .. seealso:: :meth:`asyncio.wait`
        """
        s: Set[asyncio.Task] = set()
        for i in hook_cls:
            s.update(self._tasks[i])
        if not s:
            return set(), set()
        r = await asyncio.wait(s, timeout=timeout)
        if timeout is None and any(self._tasks[i] for i in hook_cls):
            # await potential new tasks in these sets, only if no timeout.
            r2 = await self.wait(*hook_cls)
            return set(chain(r[0], r2[0])), set()
        return r

    def clear(self, *hook_cls: str, cancel: bool = True):
        """Clear the given task sets

        :param hook_cls: task class names
        :param cancel: Cancel the task if a set is not empty, defaults to True. Else will just clear the ref.
        """
        for i in hook_cls:
            s = self._tasks[i]
            if s and not cancel:
                # dangerous
                s.clear()
                continue
            for t in s:
                t.cancel()  # done callback will remove the task from this set


class Emittable(Tasksets, Generic[Evt]):
    hook: Union[Evt, NullEvent] = NullEvent()

    def register_hook(self, hook: Evt):
        assert not isinstance(hook, NullEvent)
        self.hook = hook


class EventManager:
    """EventManager is a convenient way to create/trace/manage friend classes."""

    __orig_bases__: Dict[Type[Event], Type[Event]]
    """Keys as base classes, values as their subclasses."""
    __bases_init__: bool
    """The `__orig_bases__` has been updated using :meth:`_update_bases`."""

    def sub_of(self, event: Type[Evt]) -> Type[Evt]:
        """Use this method to get current inheritence from an ancestor which was given to the
        factory.

        >>> class Mgr(EventManager[Event1, Event2]): pass
        >>> m = Mgr()
        >>> m.sub_of(Event1)    # must be one of Event1, Event2
        Event1
        """
        return self.__orig_bases__[event]  # type: ignore

    def __repr__(self) -> str:
        return f"EventManager of {self.__orig_bases__}"

    def __class_getitem__(cls, events: List[Type[Event]]):
        """Factory."""

        name = "evtmgr_" + "_".join(i.__name__.lower() for i in events)
        return type(
            name,
            (cls,),
            dict(
                __orig_bases__={i: i for i in events},
                __bases_init__=False,
            ),
        )

    def _get_sub_func(self, ty: Type[Evt]) -> Optional[Callable[[Type[Evt]], Type[Evt]]]:
        """Given a event type, returns a method in which a subclass is returned.
        By default these methods should be named as `_sub_xxxx` (lowercase). One may
        override this method to change this manner.

        .. code-block:: python
            :caption: Example
            :linenos:

            class Mgr(EventManager[Event1]):
                def _sub_event1(self, base):
                    class my_event1(base): ...
                    return my_event1

        :meta public:
        """
        return getattr(self, f"_sub_{ty.__name__.lower()}", None)

    def __init__(self) -> None:
        self._update_bases()

    def _update_bases(self):
        """Update bases. Could be called multiple times if the manager is subclassed.

        .. code-block:: python
            :caption: Example
            :linenos:

            class BaseMgr(EventManager[Event1]):
                def _sub_event1(self, base):
                    class basemgr_event1(base): ...
                def __init__(self):
                    # call _update_bases the first time, update event1 to basemgr_event1
                    super().__init__()

            class SubMgr(BaseMgr):
                def _sub_event1(self, base):
                    class submgr_event1(base): ...
                def __init__(self):
                    # call _update_bases the second time, update basemgr_event1 to submgr_event1
                    super().__init__()

        :meta public:
        """
        if self.__bases_init__:
            return
        for k, v in self.__orig_bases__.items():
            sub_func = self._get_sub_func(k)
            if sub_func is None:
                continue
            self.__orig_bases__[k] = sub_func(v)
        self.__bases_init__ = True


def hook_guard(hook: Callable[P, Awaitable[T]]) -> Callable[P, Coroutine[Any, Any, T]]:
    """This can be used as a decorator to ensure a hook can only raise :exc:`HookError`."""
    assert not hasattr(hook, "__hook_guard__")

    @wraps(hook)
    async def guard_wrapper(*args: P.args, **kwds: P.kwargs) -> T:
        try:
            return await hook(*args, **kwds)
        except (BaseException, Exception) as e:  # Exception to catch ExceptionGroup
            raise HookError(hook) from e

    setattr(guard_wrapper, "__hook_guard__", True)
    return guard_wrapper
