import HashTable

class SymbolTable:

    def __init__(self, size) -> None:
        self.__ht = HashTable(size)

    def add(self, key):
        self.__ht.add(key)

    def contains(self, key):
        return self.__ht.contains(key)

    def remove(self, key):
        self.__ht.remove(key)

    def getPosition(self, key):
        return self.__ht.getPosition(key)