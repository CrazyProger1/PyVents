import threading
import asyncio

from pyvents import (
    AsyncEvent,
    Event,
    EventChannel,
    ThreadedEvent,
)


class MyEventChannel(EventChannel):
    event = Event()
    async_event = AsyncEvent()
    threaded_event = ThreadedEvent()


@MyEventChannel.event.subscribe
def subscriber():
    print("Called subscriber")


@MyEventChannel.async_event.subscribe
async def async_subscriber():
    print("Called async_subscriber")


@MyEventChannel.threaded_event.subscribe
def threaded_subscriber():
    print("Called threaded_subscriber")
    print(f"Current thread: {threading.current_thread()}")


async def main():
    MyEventChannel.event.publish()
    # Called subscriber

    await MyEventChannel.async_event.publish_async()
    # Called async_subscriber

    MyEventChannel.threaded_event.publish_threaded()
    # Called threaded_subscriber
    # Current thread: <Thread(Thread-1 (threaded_subscriber), started xxxx)>


if __name__ == "__main__":
    asyncio.run(main())
