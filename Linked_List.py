"""Реализация односвязного списка, поиска в односвязном списке, итератора для односвязного списка"""


class LinkedList:
    def __init__(self, iterable=None):
        self._head = None
        self._tail = None
        self._size = 0

        if iterable is not None:
            self.extend(iterable)

    def append(self, value):
        node = LinkedList.Node(value)

        if self._size == 0:
            self._head = node
            self._tail = node
        else:
            self._tail.next = node
            self._tail = node

        self._size += 1

    def extend(self, iterable):
        for element in iterable:
            self.append(element)

    def search(self, value):
        current = self._head
        for i in range(self._size):
            if current.value == value:
                return "Value {} found, index {} in LinkedList".format(value, i)
            current = current.next
        return "Value has not found"

    def __len__(self):
        return self._size

    def __getitem__(self, index):
        if index < 0:
            index += len(self)

        if 0 >= index > len(self):
            raise IndexError('Index out of range')

        result = self._head
        for i in range(index):
            result = result.next
        return result

    def __iter__(self):
        return LinkedList.LinkedListIterator(self._head)

    class Node:
        __slots__ = ('value', 'next')

        def __init__(self, value, next=None):
            self.value = value
            self.next = next

    class LinkedListIterator:
        def __init__(self, head):
            self.next_node = head

        def __iter__(self):
            return self

        def __next__(self):
            if self.next_node is None:
                raise StopIteration
            result = self.next_node
            self.next_node = self.next_node.next
            return result.value
