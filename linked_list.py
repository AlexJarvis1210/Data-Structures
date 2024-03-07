class LinkedList:
    """
    A linked list class.

    Attributes:
        head (Node): The first node in the linked list, or None if the list is empty.
        size (int): The number of nodes in the linked list.
    """

    class Node:
        """
        A node for use in a linked list.

        Attributes:
            data (object): The data stored in the node.
            next (Node): The next node in the linked list, or None if this is the last node.
        """

        def __init__(self, data: object):
            """
            Initialise a new node with data.

            Preconditions: True.
            Input: data, an object to be stored in the node.
            Postconditions: The node is created with the given data and no next node.
            """
            self.data = data  
            self.next = None  

    def __init__(self):
        """
        Initialise a new, empty linked list.

        Preconditions: True.
        Postconditions: An empty linked list is created with a head pointing to None and size 0.
        """
        self.head = None
        self.size = 0

    def append(self, data):
        """
        Append a node to the end of the list.

        Preconditions: True
        Input: data, an object to be appended to the list.
        Postconditions: The list has one additional node at the end containing the given data.
        """
        new_node = self.Node(data)
        if self.head is None:
            self.head = new_node
            self.size += 1
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node
        self.size += 1

    def find_first(self, data):
        """
        Finds the first index of the given data. If none, raises ValueError.

        Preconditions: True
        Input: data, the object to be located in the list.
        Output: The index (int) of the node containing the data.
        Postconditions: If the data is found, returns the index of the node containing it.
                        If the data is not found, raises a ValueError.
        """
        current_node = self.head
        current_position = 0
        while current_node:
            if current_node.data == data:
                return current_position
            else:
                current_node = current_node.next
                current_position += 1
        raise ValueError(f"{data} not found in the list.")

    def find_last(self, data):
        """
        Finds the last index of the given data. If none, raises ValueError.

        Preconditions: True
        Input: data, the object to be located in the list.
        Output: The last index (int) of the node containing the data.
        Postconditions: If the data is found, returns the last index of the node containing it.
                        If the data is not found, raises a ValueError.
        """
        current_node = self.head
        current_position = 0
        last_position = -1  # Using -1 to indicate that the data hasn't been found yet.
        while current_node:
            if current_node.data == data:
                last_position = current_position
            current_node = current_node.next
            current_position += 1

        if last_position != -1:
            return last_position
        else:
            raise ValueError(f"{data} not found in the list.")

    def find_all(self, data):
        """
        Finds every index for the given data, returning a list of indices.

        Preconditions: True
        Input: data, the object to be located in the list.
        Output: A list of integers representing indices where the data is found.
        Postconditions: If the data is found, returns a list of indices. If not found, raises ValueError.
        """
        current_node = self.head
        current_position = 0
        index_found = []
        while current_node:
            if current_node.data == data:
                index_found.append(current_position)
            current_node = current_node.next
            current_position += 1
        
        if not index_found:
            raise ValueError(f"{data} not found in the list.")
        else:
            return index_found

    def get_position(self, index: int):
        """
        Retrieves the data at the specified index in the list.

        Preconditions: True
        Input: index, an integer specifying the position in the list.
        Output: The data object at the specified index.
        Postconditions: Returns the data at the specified index if it exists, or raises IndexError.
        """
        if index < 0 or index >= self.size:
            raise IndexError("Index outside of list range")
        current_position = 0
        current_node = self.head
        while current_node and current_position < index:
            current_node = current_node.next
            current_position += 1

        return current_node.data if current_node else None

    def from_array(self, array):
        """
        Converts an array into a linked list.

        Preconditions: True
        Input: array, a list of objects to be converted into a linked list.
        Postconditions: The current linked list represents the sequence of elements in the array.
                        If the array is empty, raises TypeError.
        """
        if not isinstance(array, list):
            raise TypeError("Expected a list")
        
        for data in array:
            self.append(data)
    
    def from_dict(self, input_dict):
        """
        Creates a linked list from the key-value pairs of a given dictionary.

        Preconditions: True
        Input: input_dict, a dictionary whose key-value pairs will be used to create the linked list.
        Postconditions: A linked list is created with nodes containing the key-value pairs from the input dictionary.
                        If the input is not a dictionary, raises TypeError.
        """
        if not isinstance(input_dict, dict):
            raise TypeError("Expected a dictionary")

        for key, value in input_dict.items():
            self.append((key, value))
    
    def convert_str(self, string: str):
        """
        Converts a string into a linked list, where each node contains a character.

        Preconditions: True
        Input: string, a string to be converted into a linked list.
        Postconditions: The current linked list represents the sequence of characters in the string.
                        If the input is not a string, raises TypeError.
        """
        if not isinstance(string, str):
            raise TypeError("Expected a string")

        for char in string:
            self.append(char)

    def create_array(self):
        """
        Converts the linked list into an array.

        Preconditions: True
        Output: An array containing the data from the linked list nodes.
        Postconditions: Returns an array representing the sequence of elements in the linked list.
        """
        current_node = self.head
        array = []
        while current_node:
            array.append(current_node.data)
            current_node = current_node.next
        return array

    def insert(self, index, data):
        """
        Inserts data at a specified index in the list.

        Preconditions: True
        Input: 
            - index, an integer specifying the position in the list where the data should be inserted.
            - data, the object to be inserted in the list.
        Postconditions: The data is inserted at the specified position, or an error is raised if the index is invalid.
        """
        if index < 0:
            raise IndexError("Position < 0")
        if index > self.size:
            raise ValueError("Position > size of list")
        
        new_node = self.Node(data)  # Updated to self.Node
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current_node = self.head
            for _ in range(index - 1):
                if current_node is None:
                    raise IndexError("Position exceeds list size")
                current_node = current_node.next
            new_node.next = current_node.next
            current_node.next = new_node
        self.size += 1
     
    def insert_after(self, data, new_data):
        """
        Inserts new data immediately after the first occurrence of specified data in the list.

        Preconditions: True
        Input: 
            - data, the object after which the new data should be inserted.
            - new_data, the object to be inserted in the list.
        Postconditions: The new data is inserted immediately after the first occurrence of specified data,
                        or does nothing if the specified data is not found.
        """
        new_node = self.Node(new_data)
        current_node = self.head

        while current_node:
            if current_node.data == data:
                new_node.next = current_node.next
                current_node.next = new_node
                self.size += 1
                break
            current_node = current_node.next

    def insert_array(self, index, array):
        """
        Inserts an array of data at a specified index in the list.

        Preconditions: True
        Input: 
            - index, an integer specifying the position in the list where the array should be inserted.
            - array, a list of objects to be inserted into the list.
        Postconditions: The data from the array is inserted at the specified position,
                        or an error is raised if the index is invalid or input is not an array.
        """
        if not isinstance(array, list):
            raise TypeError("Input is not an array")
        if index < 0 or index > self.size:
            raise ValueError("Index outside of list range")

        if index == 0:
            old_head = self.head
            for data in array[::-1]:  # Reverse the array to maintain order when inserting at the head
                new_node = self.Node(data)
                new_node.next = old_head
                self.head = new_node
            self.size += len(array)
        else:
            current_node = self.head
            for _ in range(index - 1):
                current_node = current_node.next
            splice_end = current_node.next

            for data in array:
                new_node = self.Node(data)
                current_node.next = new_node
                current_node = new_node
            current_node.next = splice_end
            self.size += len(array)

    def delete_item(self, index):
        """
        Deletes the item at the specified index from the list.

        Preconditions: True
        Input: index, an integer indicating the position of the item to be deleted.
        Postconditions: The item at the specified index is removed from the list,
                        or an error is raised if the index is invalid.
        """
        if index < 0 or index >= self.size:
            raise IndexError("Index outside of list range")
        if index == 0:
            self.head = self.head.next
        else:
            current_node = self.head
            for _ in range(index - 1):
                current_node = current_node.next
            current_node.next = current_node.next.next if current_node.next else None
        self.size -= 1

    def replace_position(self, index: int, data):
        """
        Replaces the data at a specified position in the list.

        Preconditions: True
        Input: 
            - index, an integer specifying the position in the list.
            - data, the new data to be placed at the specified position.
        Postconditions: The data at the specified position is replaced,
                        or an error is raised if the index is invalid.
        """
        if index < 0 or index >= self.size:
            raise IndexError("Index outside of list range")

        current_node = self.head
        for _ in range(index):
            current_node = current_node.next

        current_node.data = data if current_node else None

    def replace_all(self, old, new):
        """
        Replaces all occurrences of a specified value with a new value in the list.

        Preconditions: True
        Input: 
            - old, the value to be replaced.
            - new, the value to replace with.
        Postconditions: All instances of 'old' in the list are replaced with 'new'.
        """
        current_node = self.head
        while current_node:
            if current_node.data == old:
                current_node.data = new
            current_node = current_node.next

    def clear_all(self, confirm=False):
        """
        Clears all elements from the linked list.

        Preconditions: True
        Input: confirm, a boolean indicating whether to proceed with clearing the list.
        Postconditions: If confirm is True, the list is cleared; otherwise, nothing happens.
        """
        if confirm:
            self.head = None
            self.size = 0
        else:
            print("Clear operation cancelled. Set confirm=True to clear the list.")

    def print(self):
        """
        Prints the elements of the linked list.

        Preconditions: True
        Output: Prints each element of the list followed by an arrow, ending with 'None'.
        Postconditions: The elements of the list are printed to the console.
        """
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")


