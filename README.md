# PyVents

<p align="center">
<a href="https://github.com/CrazyProger1/PyVents/blob/master/LICENSE"><img alt="GitHub" src="https://img.shields.io/github/license/CrazyProger1/PyVents"></a>
<a href="https://github.com/CrazyProger1/PyVents/releases/latest"><img alt="GitHub release (latest by date)" src="https://img.shields.io/github/v/release/CrazyProger1/PyVents"></a>
<a href="https://pypi.org/project/pyvents/"><img alt="PyPI - Downloads" src="https://img.shields.io/pypi/dm/pyvents"></a>
<a href="https://github.com/psf/black"><img src="https://img.shields.io/badge/code%20style-black-000000.svg" alt="Code Style"></a>
<img src="https://img.shields.io/badge/coverage-100%25-brightgreen" alt="Coverage"/>
</p>


PyVents is a powerful Python library for events.

## Features

## Installation

Using pip:

```shell
pip install pyvents
```

Using Poetry:

```shell
poetry add pyvents
```

## Getting-Started

See [examples](examples) for more.

### Simple

```python
from pyvents import Event

event = Event("myevent")


def subscriber():
    print("Called subscriber")


def main():
    event.subscribe(subscriber)
    event.publish()
    # Called subscriber


if __name__ == '__main__':
    main()
```

### Advanced

```python
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
```

## Status

`0.0.1` - **RELEASED**

## License

PyVents is released under the MIT License. See the bundled [LICENSE](LICENSE) file for details.