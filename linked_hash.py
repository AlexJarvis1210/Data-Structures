from linked_list import LinkedList

class LinkedHash:
    def __init__(self):
        """
        Initialise a new, empty LinkedHash.

        Preconditions: True
        Postconditions: An empty LinkedHash is created with a single, empty Linked List.
        """
        self.size = 1
        self.total_elements = 0
        self.hash_linked = [LinkedList()]

    def associate(self, key: object, value: object) -> None:
        """
        Associate a key with a value in the hash table.

        Preconditions: True
        Input: 
            - key, the key to associate with the value.
            - value, the value to be associated with the key.
        Postconditions: The key-value pair is added to the hash table, replacing the old value if the key already exists.
        """
        self.change_size()
        index = hash(key) % len(self.hash_linked)
        current_list = self.hash_linked[index]
        for i, (k, _) in enumerate(current_list.create_array()):
            if k == key:
                current_list.replace_position(i, (key, value))
                return
        current_list.append((key, value))
        self.total_elements += 1

    def change_size(self) -> None:
        """
        Dynamically grows or shrinks the size of the hash table to maintain efficient operations.

        Postconditions:
        - If pre-self has a load factor > 0.7, post-self has a larger hash table, reducing the load factor.
        - If pre-self has a load factor < 0.3, post-self has a smaller hash table, increasing the load factor.
        """
        load_factor = self.total_elements / len(self.hash_linked)
        new_capacity = 0

        if load_factor > 0.7:
            new_capacity = len(self.hash_linked) * 2
        elif load_factor < 0.3 and len(self.hash_linked) > 10: 
            new_capacity = len(self.hash_linked) // 2

        if new_capacity:
            new_hash = [LinkedList() for _ in range(new_capacity)]
            for linked_list in self.hash_linked:
                for (key, value) in linked_list.create_array():
                    index = hash(key) % new_capacity
                    new_hash[index].append((key, value))
            self.hash_linked = new_hash
            self.size = new_capacity

    def get(self, key: object) -> object:
        """
        Retrieves the value associated with a given key, if it exists.

        Preconditions: True 
        Input: key, the key whose associated value is to be returned.
        Output: The value associated with the given key, if it exists.
        Postconditions: Returns the value associated with the given key, if one exists.
        """
        index = hash(key) % len(self.hash_linked)
        current_list = self.hash_linked[index]
        for k, v in current_list.create_array():
            if k == key:
                return v
        raise KeyError(f"Key '{key}' not found in LinkedHash.")

    def has(self, key: object) -> bool:
        """
        Checks if a key is present in the hash table.

        Preconditions: key is hashable
        Returns: True if the key is in the hash table; False otherwise.
        """
        index = hash(key) % len(self.hash_linked)
        current_list = self.hash_linked[index]
        for k, _ in current_list.create_array():
            if k == key:
                return True
        return False

    def print(self):
        """
        Prints out the elements in each linked list of the hash array.

        Preconditions: True
        Output: Prints the contents of each slot in the hash table.
        Postconditions: The contents of the hash table are printed to the console.
        """
        for i, linked_list in enumerate(self.hash_linked):
            print(f"Slot {i}: ", end="")
            linked_list.print()