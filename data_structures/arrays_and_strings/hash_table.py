from data_structures.linked_list.singly_linked_list import LinkedList


class HashEntry():
    """Class to represent the key, value pair stored in a hash table
    """

    def __init__(self, key, value):
        """Store key and value

        Parameters
        ----------
        key
            Key in key value store. Can be any non-mutable data type
        value
            Can be any python object
        """
        self.key = key
        self.value = value

    def __str__(self):
        """Overload __str__ so something sensible is printed

        Returns
        -------
        print_string : str
            Key and value of object, in nicely formatted string
        """
        print_string = 'key: {}   |   value: {}'.format(
            str(self.key), str(self.value)
        )
        return print_string


class HashTable():
    """Class to represent a hash table object
    """

    def __init__(self, num_elements):

        """Initialise Hash Table by creating array of length num_elements, with
        each element being a linked list

        Parameters
        ----------
        num_elements : int
            Size of array that stores linked lists
        """

        # Create array of linked lists
        self.main_array = [LinkedList() for i in range(num_elements)]
        self.num_elements = num_elements

    def _key_hash(self, key):
        """"Hash function to map input key to an integer, which represents the
        index in the main_array that contains the linked list which contains
        the input key, value pair.

        Built on top of python's built in hash() function. Note, for strings,
        python's hash() function will hash to a different result each time the
        python process is run, since it salts the input with a random string.
        Results will be consistent within the same python process.

        Parameters
        ----------
        key
            Key in key value store. Can be any non-mutable data type

        Returns
        -------
        int
            Hashed key, representing an index in self.main_array
        """

        # Hash key with Python's built-in hash function (returns and integer)
        py_hashed_key = hash(key)

        # Map to an index in main_array
        # Note: len() is O(1) constant time in Python
        return py_hashed_key % len(self.main_array)

    def insert(self, key, value):
        """Insert key, value pair into hash table

        Parameters
        ----------
        key
            Key in key value store. Can be any non-mutable data type
        value
            Can be any python object
        """

        # Map key to an index in main_array
        item_index = self._key_hash(key)

        # Turn input key, value pair into a HashEntry object
        data = HashEntry(key, value)

        # Append key, value pair to end of appropriate linked list
        self.main_array[item_index].append(data)

    def _linked_list_lookup(self, linked_list, key):
        """Returns value corresponds to input key in a linked list, raising a
        KeyError if key not found

        Parameters
        ----------
        linked_list : LinkedList
            LinkedList object in which to perform lookup
        key
            Key in key value store (un-hashed). Can be any non-mutable data
            type

        Returns
        -------
        current_node.data.value
            Value corresponding to input key. Can be any python object.
        """

        # Handle special case of empty linked list
        if linked_list.head is None:
            raise KeyError('Key not found in hash table.')

        # Start at head node (beginning of linked list)
        current_node = linked_list.head

        # Special case of key being at head node
        if current_node.data.key == key:
            return current_node.data.value

        # Iterate through linked list until key is found, or end is reached
        while current_node.next_node is not None:

            # Go to next node
            current_node = current_node.next_node

            # Check if current node corresponds to input key
            if current_node.data.key == key:
                return current_node.data.value

        # Raise KeyError if key not found in linked list
        raise KeyError('Key not found in hash table.')

    def retrieve(self, key):
        """Retrieve a value from the hash table based on its key

        Parameters
        ----------
        key
            Key in key value store (un-hashed). Can be any non-mutable data
            type

        Returns
        -------
        Value corresponding to input key. Can be any python object.
        """

        # Map key to an index in main_array
        item_index = self._key_hash(key)

        # Retrieve corresponding linked list
        bucket = self.main_array[item_index]

        # Lookup key in linked list, returning its value
        return self._linked_list_lookup(bucket, key)

    def print_all(self):
        """Print entire contents of hash table
        """
        print(
            """\nContents of hash table, with blank lines separating distinct
            linked lists:""".replace('  ', ''))

        for linked_list in self.main_array:
            linked_list.print_all()
            print('')


if __name__ == '__main__':

    h = HashTable(10)

    h.insert(-88, 'minus eighty-eight')
    h.insert(0, 'zero')
    h.insert(7, 'seven')
    h.insert(8, 'eight')
    h.insert(10, 'ten')
    h.insert(490, 'four hundred and ninety')
    h.insert(99, 'ninety-nine')
    print(h.retrieve(7))
    print(h.retrieve(99))

    h.print_all()
