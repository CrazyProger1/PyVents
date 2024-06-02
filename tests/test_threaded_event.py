import threading

from pyvents import ThreadedEvent


def test_publish_threaded():
    ev = ThreadedEvent(name="test")

    def subs():
        assert threading.current_thread() is not threading.main_thread()

    ev.subscribe(subs)

    ev.publish_threaded()
