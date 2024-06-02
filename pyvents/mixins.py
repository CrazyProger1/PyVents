from .events import AsyncEvent, ThreadedEvent


class AsyncThreadedEvent(AsyncEvent, ThreadedEvent):
    def __init__(self, name: str | None = None, **kwargs):  # pragma: nocover
        AsyncEvent.__init__(self, name=name, **kwargs)
        ThreadedEvent.__init__(self, name=name, **kwargs)
