#!python

from linkedlist import LinkedList


# Implement LinkedStack below, then change the assignment at the bottom
# to use this Stack implementation to verify it passes all tests
class LinkedStack(LinkedList):

    def __init__(self, iterable=None):
        """Initialize this stack and push the given items, if any."""
        # Initialize a new linked list to store the items
        super().__init__()
        self.top = self.head # rename 
        if iterable is not None: 
            for item in iterable:
                self.push(item)

    def __repr__(self):
        """Return a string representation of this stack."""
        return 'Stack({} items, top={})'.format(self.length(), self.peek())

    def is_empty(self):
        """Return True if this stack is empty, or False otherwise."""
        # TODO: Check if empty
        if self.head == None:
            return True
        else:
            return False

    def length(self):
        """Return the number of items in this stack."""
        # TODO: Count number of items
        return self.size

    def push(self, item):
        """Insert the given item on the top of this stack.
        Running time: O(???) – Why? [TODO]"""
        # TODO: Push given item
        self.prepend(item)

    def peek(self):
        """Return the item on the top of this stack without removing it,
        or None if this stack is empty."""
        # TODO: Return top item, if any
        try:
            return self.head.data
        except AttributeError:
            return None

    def pop(self):
        """Remove and return the item on the top of this stack,
        or raise ValueError if this stack is empty.
        Running time: O(???) – Why? [TODO]"""
        # TODO: Remove and return top item, if any
        try:
            popped = self.head
            self.head = self.head.next
            self.size -= 1
            return popped.data
        except AttributeError:
            raise ValueError("Stack is empty")
    

# Implement ArrayStack below, then change the assignment at the bottom
# to use this Stack implementation to verify it passes all tests
class ArrayStack(list):

    def __init__(self, iterable=None):
        """Initialize this stack and push the given items, if any."""
        # Initialize a new list (dynamic array) to store the items
        super().__init__() 

        if iterable is not None:
            for item in iterable:
                self.push(item)

    def __repr__(self):
        """Return a string representation of this stack."""
        return 'Stack({} items, top={})'.format(self.length(), self.peek())

    def is_empty(self):
        """Return True if this stack is empty, or False otherwise."""
        # TODO: Check if empty
        if self != []:
            return False
        else:
            return True

    def length(self):
        """Return the number of items in this stack."""
        # TODO: Count number of items
        return len(self)

    def push(self, item):
        """Insert the given item on the top of this stack.
        Running time: O(???) – Why? [TODO]"""
        # TODO: Insert given item
        self.append(item)

    def peek(self):
        """Return the item on the top of this stack without removing it,
        or None if this stack is empty."""
        # TODO: Return top item, if any
        try:
            return self[-1]
        except IndexError:
            return None

    # def pop(self):
    #     """Remove and return the item on the top of this stack,
    #     or raise ValueError if this stack is empty.
    #     Running time: O(???) – Why? [TODO]"""
    #     # TODO: Remove and return top item, if any
    #     item = self[-1]

    #     # weird stuff happening here
    #     # Print statements suggest everything is working correctly but the tests are failing
    #     # print("Popping: ", item)
    #     # print("New top should be", self[-2])
    #     # self = self[0:-1] # whoops this is broken
    #     # print("new top is: ", self.peek())
    #     item = self.peek()
    #     self.remove(item)
    #     return item


# Implement LinkedStack and ArrayStack above, then change the assignment below
# to use each of your Stack implementations to verify they each pass all tests
# Stack = LinkedStack
Stack = ArrayStack