# https://refactoring.guru/design-patterns/singleton

from threading import Lock, Thread


class Singleton:
    _instance = None
    _lock = Lock()

    def __new__(cls, value: str):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls)
                cls._instance.value = value
        return cls._instance


def test_singleton(value: str):
    singleton = Singleton(value)
    print(singleton.value)


if __name__ == "__main__":
    print("If you see the same value, then singleton was reused (yay!)\n"
          "If you see different values, then 2 singletons were created (booo!!)\n\n"
          "RESULT:\n")

    t1 = Thread(target=test_singleton, args=("FOO",))
    t2 = Thread(target=test_singleton, args=("BAR",))
    t1.start()
    t2.start()
