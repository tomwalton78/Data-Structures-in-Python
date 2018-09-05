from data_structures.linked_lists.singly_linked_list import LinkedList


class Stack(LinkedList):
    """Class to represent a stack data structure.

    Wraps the LinkedList class. The head node of the linked list is treated as the
    top of the stack, and data can only be added by appending.
    """

    def pop(self):
        pass

    def push(self, data):
        pass

    def peek(self):
        pass

    def is_empty(self):
        pass

    def prepend(self):
        """Overwrite 'prepend' method of LinkedList class to raise an
        exception, since not appropriate for the Stack class.
        """
        raise AttributeError("'Stack' object has no attribute 'prepend'")

    def delete_first_node_with_value(self):
        """Overwrite 'delete_first_node_with_value' method of LinkedList class
        to raise an exception, since not appropriate for the Stack class.
        """
        raise AttributeError(
            "'Stack' object has no attribute 'delete_first_node_with_value'"
        )
