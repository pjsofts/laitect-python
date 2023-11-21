class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self, value):
        for observer in self._observers:
            observer.update(value)


class Observer:
    def update(self, value):
        print(f"Received value: {value}")


# Usage
subject = Subject()
observer1 = Observer()
observer2 = Observer()

subject.attach(observer1)
subject.attach(observer2)

subject.notify("Hello Observers!")
subject.notify("salam")