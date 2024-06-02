from abc import ABC, ABCMeta, abstractmethod
from typing import Callable, Collection


class BaseEventChannelMetaclass(ABCMeta):
    __events__: dict[str, "BaseEvent"]

    @property
    @abstractmethod
    def events(cls) -> Collection["BaseEvent"]: ...

    @abstractmethod
    def __contains__(self, event: str) -> bool: ...

    @abstractmethod
    def __repr__(cls): ...

    @abstractmethod
    def __getitem__(self, event: str) -> "BaseEvent": ...

    @abstractmethod
    def __iter__(self): ...


class BaseEventChannel(metaclass=BaseEventChannelMetaclass):
    pass


class BaseEvent(ABC):
    @property
    @abstractmethod
    def name(self) -> str: ...

    @property
    @abstractmethod
    def channel(self) -> type[BaseEventChannel] | None: ...

    @property
    @abstractmethod
    def subscribers(self) -> Collection[Callable]: ...

    @abstractmethod
    def subscribe(self, callback: Callable) -> Callable: ...

    @abstractmethod
    def unsubscribe(self, callback: Callable) -> None: ...

    @abstractmethod
    def is_subscriber(self, callback: Callable) -> bool: ...

    @abstractmethod
    def publish(self, *args, **kwargs) -> None: ...

    @abstractmethod
    def __repr__(self): ...


class BaseAsyncEvent(BaseEvent):
    @abstractmethod
    async def publish_async(self, *args, **kwargs) -> None: ...


class BaseThreadedEvent(BaseEvent):
    @abstractmethod
    def publish_threaded(self, *args, **kwargs) -> None: ...
