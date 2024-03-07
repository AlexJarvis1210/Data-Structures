from linked_list import LinkedList

class LinkedStack:
    """
    A stack data structure implementing LIFO (Last In First Out) behavior using a linked list.
    """

    def __init__(self):
        """
        Initialise a new, empty LinkedStack.

        Preconditions: True
        Post conditions: An empty LinkedStack is created.
        """
        self._list = LinkedList()

    def push(self, data):
        """
        Adds a data item to the top of the stack.

        Preconditions: True
        Input: data, the data to be pushed onto the stack.
        Postconditions: The data is added to the top of the stack.
        """
        self._list.insert(0, data)

    def pop(self):
        """
        Removes and returns the top item from the stack.

        Preconditions: The stack is not empty.
        Output: The data that was at the top of the stack.
        Postconditions: The top item is removed from the stack. If the stack was empty, raises IndexError.
        """
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        value = self._list.get_position(0)
        self._list.delete_item(0)
        return value

    def peek(self):
        """
        Returns the top item from the stack without removing it.

        Preconditions: The stack is not empty.
        Output: The data that is at the top of the stack.
        Postconditions: The top item of the stack is returned, but the stack remains unchanged. If the stack is empty, raises IndexError.
        """
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self._list.get_position(0)

    def is_empty(self):
        """
        Checks whether the stack is empty.

        Preconditions: True
        Output: Returns True if the stack is empty; otherwise, False.
        Postconditions: The stack remains unchanged.
        """
        return self._list.head is None

    def size(self):
        """
        Returns the number of items in the stack.

        Preconditions: True
        Output: The size of the stack as an integer.
        Postconditions: The stack remains unchanged.
        """
        return self._list.size

    def print_stack(self):
        """
        Prints the items in the stack from top to bottom.

        Preconditions: True
        Output: The items in the stack are printed to the console.
        Postconditions: The stack remains unchanged.
        """
        self._list.print()
