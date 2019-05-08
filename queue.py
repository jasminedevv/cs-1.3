#!python

from linkedlist import LinkedList, Node


# Implement LinkedQueue below, then change the assignment at the bottom
# to use this Queue implementation to verify it passes all tests
class LinkedQueue(LinkedList):

    def __init__(self, iterable=None):
        """Initialize this queue and enqueue the given items, if any."""
        # Initialize a new linked list to store the items
        super().__init__()
        if iterable is not None:
            for item in iterable:
                self.enqueue(item)

    def __repr__(self):
        """Return a string representation of this queue."""
        return 'Queue({} items, front={})'.format(self.length(), self.front())

    def is_empty(self):
        """Return True if this queue is empty, or False otherwise."""
        if self.head is None:
            return True
        else:
            return False

    def length(self):
        """Return the number of items in this queue."""
        length = 0
        node = self.head
        while node is not None:
            node = node.next
            length += 1
        return length


    def enqueue(self, item):
        """Insert the given item at the back of this queue.
        Running time: O(???) – Why? [TODO]"""
        new_node = Node(item)
        try:
            self.tail.next = new_node
        except AttributeError: # queue is empty
            self.head = new_node
            self.tail = new_node

        self.tail = new_node

    def front(self):
        """Return the item at the front of this queue without removing it,
        or None if this queue is empty."""
        try:
            return self.head.data
        except AttributeError:
            return None

    def dequeue(self):
        """Remove and return the item at the front of this queue,
        or raise ValueError if this queue is empty.
        Running time: O(???) – Why? [TODO]"""
        node = self.head
        try:
            self.head = self.head.next
        except AttributeError:
            raise ValueError
        return node.data


# Implement ArrayQueue below, then change the assignment at the bottom
# to use this Queue implementation to verify it passes all tests
class ArrayQueue(list):

    def __init__(self, iterable=None):
        """Initialize this queue and enqueue the given items, if any."""
        # Initialize a new list (dynamic array) to store the items
        super().__init__()
        if iterable is not None:
            for item in iterable:
                self.enqueue(item)

    def __repr__(self):
        """Return a string representation of this queue."""
        return 'Queue({} items, front={})'.format(self.length(), self.front())

    def is_empty(self):
        """Return True if this queue is empty, or False otherwise."""
        if self == []:
            return True
        else:
            return False

    def length(self):
        """Return the number of items in this queue."""
        return len(self)

    def enqueue(self, item):
        """Insert the given item at the back of this queue.
        Running time: O(???) – Why? [TODO]"""
        self.append(item)

    def front(self):
        """Return the item at the front of this queue without removing it,
        or None if this queue is empty."""
        try:
            return self[0]
        except IndexError:
            return None

    def dequeue(self):
        """Remove and return the item at the front of this queue,
        or raise ValueError if this queue is empty.
        Running time: O(???) – Why? [TODO]"""
        try:
            return self.pop(0)
        except IndexError:
            raise ValueError


# Implement LinkedQueue and ArrayQueue above, then change the assignment below
# to use each of your Queue implementations to verify they each pass all tests
# Queue = LinkedQueue
Queue = ArrayQueue