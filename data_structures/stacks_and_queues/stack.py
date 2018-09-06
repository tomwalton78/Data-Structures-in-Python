from data_structures.linked_lists.singly_linked_list import LinkedList


class Stack(LinkedList):
    """Class to represent a stack data structure.

    Wraps the LinkedList class. The head node of the linked list is treated as
    the of the stack, and data can only be added by prepending.
    """

    def _delete_head(self):
        """Delete head node of LinkedList.
        """
        self.head = self.head.next_node

    def pop(self):
        """Remove and return the top item from the stack.

        Returns
        -------
            Data at head of LinkedList
        """
        if self.is_empty():
            raise Exception('{} is empty.'.format(self.__name__))

        # Retrieve head node data, then delete head node
        data = self.head.data
        self._delete_head()

        return data

    def push(self, data):
        """Add item (data) to top of stack (i.e. to head of LinkedList).

        Parameters
        ----------
        data
            Data to store in stack.
        """
        self.prepend(data)

    def peek(self):
        """Return item at top of stack, throwing exception if stack is empty.

        Returns
        -------
            Data at head of LinkedList
        """

        if self.is_empty():
            raise Exception('{} is empty.'.format(self.__name__))

        return self.head.data

    def is_empty(self):
        """Return True if stack is empty, False if not.
        """
        if self.head is None:
            return True
        else:
            return False

    def append(self):
        """Overwrite 'append' method of LinkedList class to raise an
        exception, since not appropriate for the Stack class.
        """
        raise AttributeError("'Stack' object has no attribute 'append'")

    def delete_first_node_with_value(self):
        """Overwrite 'delete_first_node_with_value' method of LinkedList class
        to raise an exception, since not appropriate for the Stack class.
        """
        raise AttributeError(
            "'Stack' object has no attribute 'delete_first_node_with_value'"
        )

    def __str__(self):
        """Overload __str__ operator to print all values in Stack.

        Returns
        -------
        str
            Heading line, then comma separated list of Stack contents
        """

        # Retrieve result of __str__ from LinkedList class
        base_string = super().__str__()

        # Handle empty stack
        if base_string == 'LinkedList is empty':
            return 'Stack is empty'

        # Remove heading, only need contents
        contents = base_string.split('\n')[1]

        # Set different heading for Stack class
        heading = 'Stack contents: top -> bottom\n'

        return ''.join([heading, contents])


if __name__ == '__main__':

    s = Stack()

    [s.push(i) for i in range(5)]

    print(s)

    print('peek:', s.peek())

    print('Removed:', s.pop(), s.pop(), s.pop())

    print(s)

    print('Is stack empty?', s.is_empty())

    print('Removed:', s.pop(), s.pop())
    print(s)
    print('Is stack empty?', s.is_empty())
