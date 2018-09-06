from data_structures.linked_lists.singly_linked_list import LinkedList
from data_structures.stacks_and_queues.stack import Stack


class Queue(Stack):
    """Class to represent a Queue data structure.

    Inherits from Stack class, since these two data structures are very
    similar. Stack inherits from LinkedList class.
    """

    def add(self, data):
        """Add item to end of queue.

        Uses append method of LinkedList base class.
        """
        super(Stack, self).append(data)

    def remove(self):
        """Remove and return first item in queue.

        Returns
        -------
            Data at head of LinkedList
        """
        return self.pop()

    def __str__(self):
        """Overload __str__ operator to print all values in Queue.

        Returns
        -------
        str
            Heading line, then comma separated list of Queue contents
        """

        # Retrieve result of __str__ from LinkedList class
        base_string = super().__str__()

        # Handle empty stack
        if base_string == 'Stack is empty':
            return 'Queue is empty'

        # Remove heading, only need contents
        contents = base_string.split('\n')[1]

        # Set different heading for Stack class
        heading = 'Queue contents: front -> back\n'

        return ''.join([heading, contents])


if __name__ == '__main__':

    q = Queue()

    [q.add(i) for i in range(5)]

    print(q)

    print('peek:', q.peek())

    print('Removed:', q.remove(), q.remove(), q.remove())

    print(q)

    print('Is queue empty?', q.is_empty())

    print('Removed:', q.remove(), q.remove())
    print(q)
    print('Is queue empty?', q.is_empty())
