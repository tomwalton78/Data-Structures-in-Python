class MinHeap():
    """Class to represent a min-heap data structure.

    Structured as a list containing all the nodes. Since every level is filled,
    before going deeper to the next level, one knows where a node is in the
    tree based on its index. Minimum element at top/root of heap, with
    remaining elements in ascending order down the heap.
    """

    def __init__(self):
        """Initialise heap with empty list to contain elements
        """
        self.main_array = []

    def _get_left_child_index(self, parent_index):
        return (2 * parent_index) + 1

    def _get_right_child_index(self, parent_index):
        return (2 * parent_index) + 2

    def _get_parent_index(self, child_index):
        return int((child_index - 1) / 2)

    def _has_left_child(self, parent_index):
        return self._get_left_child_index(parent_index) < len(self.main_array)

    def _has_right_child(self, parent_index):
        return self._get_right_child_index(parent_index) < len(self.main_array)

    def _has_parent(self, child_index):
        return self._get_parent_index(child_index) >= 0

    def _get_left_child(self, parent_index):
        return self.main_array[self._get_left_child_index(parent_index)]

    def _get_right_child(self, parent_index):
        return self.main_array[self._get_right_child_index(parent_index)]

    def _get_parent(self, child_index):
        return self.main_array[self._get_parent_index(child_index)]

    def _swap(self, index_1, index_2):
        """Swaps values at index_1 and index_2 in main_array
        """
        temp = self.main_array[index_1]
        self.main_array[index_1] = self.main_array[index_2]
        self.main_array[index_2] = temp

    def _ensure_not_empty(self):
        """Raise error if heap is empty.
        """
        if len(self.main_array) == 0:
            raise Exception('Heap is empty')

    def peek(self):
        """Return root node of heap; i.e. minimum element of aray

        Returns
        -------
        any
            Minimum element of array, can be any data type that allows greater
            than and less than comparison
        """

        # Handle empty heap
        self._ensure_not_empty()

        return self.main_array[0]

    def poll(self):
        """Remove and return minimum element, and adjust elements in heap to
        maintain ordering.

        Returns
        -------
        any
            Minimum element of array. Can be any Python object that allows
            comparison.
        """

        # Handle empty heap
        self._ensure_not_empty()

        # Extract min element before re-ordering
        min_element = self.main_array[0]

        # Move last element to root/top of heap
        self.main_array[0] = self.main_array[-1]
        self.main_array = self.main_array[:-1]

        # 'Bubble down' element to maintain heap ordering
        self._heapify_down()

        return min_element

    def insert(self, data):
        """Insert element into array.

        Insert at end, then 'bubble up' heap to maintain ordering.

        Parameters
        ----------
        data : any
            Data to insert. Can be any Python object that allows comparison.
        """

        # Insert element at end of main_array (i.e. bottom of heap)
        self.main_array.append(data)

        # 'Bubble up' to maintain heap ordering
        self._heapify_up()

    def _heapify_up(self):
        """'Bubble up' last element in array to maintain heap ordering,
        swapping it with parent elements until it is in the right place.
        """

        index = len(self.main_array) - 1

        while (
            self._has_parent(index)
            & self._get_parent(index) > self.main_array[index]
        ):
            self._swap(_get_parent_index(index), index)
            index = self._get_parent_index(index)

    def _heapify_down(self):
        """'Bubble down' root/top element of heap to maintain heap ordering,
        swapping it with child elements until it is in the right place.
        """

        index = 0

        # Check that node has a left child (if it has no left child, it won't
        # have a right child, due to the way elements are inserted)
        while self._has_left_child(index):
            # Must compare to smaller of left and right child, so get index of
            # smaller child
            smaller_child_index = self._get_left_child_index(index)

            if (
                self._has_right_child(index) and
                self._get_right_child(index) < self._get_left_child(index)
            ):
                smaller_child_index = self._get_right_child_index(index)

            # Break if ordering is correct (parent smaller than child)
            if self.main_array[index] < self.main_array[smaller_child_index]:
                break
            # Otherwise, swap parent and (smaller) child
            else:
                self._swap(index, smaller_child_index)
                index = smaller_child_index

    def __str__(self):
        """Overload __str__ method to print contents of heap, from top to
        bottom (left to right on each level).
        """

        # Handle empty heap
        if len(self.main_array) == 0:
            return 'Heap is empty'
        else:
            heading = 'Heap contents:\n'
            main_array_as_str = [str(i) for i in self.main_array]
            return heading + ', '.join(main_array_as_str)


if __name__ == '__main__':

    h = MinHeap()

    print(h)

    [h.insert(i) for i in range(10)]

    print(h)

    print('Smallest element in heap:', h.peek())

    print('Removing smallest element:', h.poll())
    print(h)
    print('Smallest element in heap:', h.peek())
