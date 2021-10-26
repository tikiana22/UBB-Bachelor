from collections import deque


class HashTable:

    def __init__(self, size):
        self.__items = [deque() for _ in range(size)]
        self.__size = size

    def hash(self, key):
        sum = 0
        for chr in key:
            sum += ord(chr) - ord('0')
        return sum % self.__size

    def add(self, key):
        self.__items[self.hash(key)].append(key)

    def contains(self, key):
        return key in self.__items[self.hash(key)]

    def remove(self, key):
        self.__items[self.hash(key)].remove(key)

    def getPosition(self, key):
        listPosition = self.hash(key)
        listIndex = 0
        for item in self.__items[listPosition]:
            if item != key:
                listIndex += 1
            else:
                break
        return (listPosition, listIndex)