import sys

if sys.version_info >= (3, 11):
    from typing import Self
else:
    from typing_extensions import Self


class EventAccessor:
    __slots__= ("add", "remove", "__instance")

    def bind(self, instance, owner) -> Self:
        self.__instance = instance
        return self
    
    def add(self, instance, other) -> None:
        ...
    
    def remove(self, instance, other) -> None:
        ...

    def __iadd__(self, other) -> Self:
        self.add(self.__instance, other)
        return self
    
    def __isub__(self, other) -> Self:
        self.remove(self.__instance, other)
        return self

class accessor(property):
    def __init__(self, add, remove = None, doc: str | None = None) -> None:
        # self.__add = add
        # self.__remove = remove
        self.__e = EventAccessor()
        self.__e.add = add
        self.__doc__ = add.__doc__ if doc is None else doc
    
    def remove(self, remove) -> Self:
        self.__e.remove = remove
        return self

    def __get__(self, instance, owner: type) -> EventAccessor:
        return self.__e.bind(instance, owner)

    def __set__(self, instance, value: EventAccessor) -> None:
        assert self.__e is value

def event_add(add) -> accessor:
    return accessor(add)



class Test:

    @event_add
    def on_update(self, value) -> None:
        print(f"on_update.add({value=})")

    @on_update.remove
    def on_update(self, value) -> None:
        print(f"on_update.remove({value=})")

    def __init__(self) -> None:
        ...


obj = Test()
print("add 1")
obj.on_update += 1
print("remove 2")
obj.on_update -= 2

obj.on_update.add(obj, 1)
