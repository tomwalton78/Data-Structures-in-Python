class Node():

    def __init__(self, data, next_node=None):
        """Initialise Node object with a value (data) and a reference to the
        next node in the linked list

        Parameters
        ----------
        data
            Data to store in node. Can be any python object.
        next_node : Node, optional
            Reference to next Node object in LinkedList
        """
        self.data = data
        self.next_node = next_node


class LinkedList():

    def __init__(self):
        """Initialise LinkedList containing no data
        """
        self.head = None

    def append(self, data):
        """Append an element to the end of the linked list

        Parameters
        ----------
        data
            Data to store in LinkedList. Can be any python object.
        """

        # If head is None (i.e. empty linked list), put the data there (as
        # first element)
        if self.head is None:
            self.head = Node(data)
            return

        # Start at the head
        current_node = self.head

        # Walk through linked list until the end
        while current_node.next_node is not None:
            current_node = current_node.next_node

        # Create new node at end of linked list, containing the data to be
        # added
        current_node.next_node = Node(data)

    def prepend(self, data):
        """Add data to beginning of linked list

        Parameters
        ----------
        data
            Data to store in LinkedList. Can be any python object.
        """

        # Create new Node to represent to contain this data, with a reference
        # to the current head of the linked list
        new_head = Node(data, next_node=self.head)

        # Update the current head of the linked list to reference this new node
        self.head = new_head

    def delete_first_node_with_value(self, data):
        """Delete the first occurrence of a node with the specified value

        Parameters
        ----------
        data
            Value to delete in LinkedList. Can be any python object.
        """

        # Handle special case of empty linked list
        if self.head is None:
            return

        # Start at head node (beginning of linked list)
        current_node = self.head

        # Handle special case of first node containing the specified data, so
        # need to delete first node
        if current_node.data == data:
            self.head = self.head.next_node
            return

        # Iterate through linked list until value is found, or end is reached
        while current_node.next_node is not None:
            # Check if node after current node contains the specified data
            if current_node.next_node.data == data:
                # Skip over next node
                current_node.next_node = current_node.next_node.next_node
                return

            # Go to next node
            current_node = current_node.next_node

    def __str__(self):
        """Overload __str__ operator to print all values in LinkedList.

        Returns
        -------
        str
            Heading line, then comma separated list of LinkedList contents
        """

        # List to store LinkedList contents
        contents = []

        # Handle special case of empty linked list
        if self.head is None:
            return 'LinkedList is empty'

        # Start at head node
        current_node = self.head

        # Store value of head node
        contents.append(current_node.data)

        # Iterate through linked list until end, printing value each time
        while current_node.next_node is not None:

            # Go to next node
            current_node = current_node.next_node

            # Store node value
            contents.append(current_node.data)

        # Convert to str
        contents = [str(i) for i in contents]
        contents = ', '.join(contents)

        heading = 'LinkedList contents: head -> tail\n'

        return ''.join([heading, contents])


if __name__ == '__main__':

    # Initialise linked list
    L = LinkedList()
    print('Initial LinkedList:')
    print(L)

    # Append elements
    L.append(1)
    L.append(2)
    L.append(3)
    print('\nElements appended:')
    print(L)

    # Prepend elements
    L.prepend(0)
    L.prepend(-1)
    print('\nElements prepended')
    print(L)

    # Delete first node with value of 2
    L.delete_first_node_with_value(2)
    print('\nLinkedList with 2 deleted:')
    print(L)
