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
