def bubble_sort(array, ascending=True):
    """Sort array using bubble sort algorithm.

    Parameters
    ----------
    array : list
        List to be sorted; Can contain any Python objects that can be compared
    ascending : bool, optional
        If True sort array from smallest to largest; False -> sort array from
        largest to smallest

    Returns
    -------
    list
        Input array sorted.
    """
    # Create copy to avoid modifying array inplace
    array = array.copy()

    # Use swap_count to keep track of number of swaps on each sweep
    swap_count = 1
    # Keep track of number of times array has been iterated over
    sweep_count = 0

    # Keep sweeping through array until no swaps need to occur
    while swap_count > 0:

        # Reset swap scount at beginning of sweep
        swap_count = 0

        # for i, j in enumerate(array.copy()[:-1]):
        for i in range(len(array) - sweep_count - 1):

            # Swap pair of elements being compared if out of order
            if array[i] > array[i+1]:
                # Perform swap
                temp = array[i+1]
                array[i+1] = array[i]
                array[i] = temp

                # Increment swap count
                swap_count += 1

        # Increment sweep_count, to avoid checking elements that are already in
        # correct order, at end of array
        sweep_count += 1

    if ascending:
        return array
    else:
        # Reverse array for descending order sort
        return array[::-1]


def selection_sort(array, ascending=True):
    """Sort array using selection sort algorithm.

    Parameters
    ----------
    array : list
        List to be sorted; Can contain any Python objects that can be compared
    ascending : bool, optional
        If True sort array from smallest to largest; False -> sort array from
        largest to smallest

    Returns
    -------
    list
        Input array sorted.
    """
    # Create copy to avoid modifying array inplace
    array = array.copy()

    # Iterate through all but last element in array
    for i, j in enumerate(array.copy()[:-1]):

        # Find index of min value element out of array, starting after current
        # element
        min_val = min(array[i+1:])
        min_index = array[i+1:].index(min_val)
        # Convert to index in array (not sliced)
        min_index = i + 1 + min_index

        # Swap current element with min element, if min element is smaller
        if array[i] > min_val:
            # Perform swap
            array[min_index] = array[i]
            array[i] = min_val

    if ascending:
        return array
    else:
        # Reverse array for descending order sort
        return array[::-1]


def merge_sort(array, ascending=True):
    """Sort array using merge sort algorithm.

    Parameters
    ----------
    array : list
        List to be sorted; Can contain any Python objects that can be compared
    ascending : bool, optional
        If True sort array from smallest to largest; False -> sort array from
        largest to smallest

    Returns
    -------
    list
        Input array sorted.
    """

    def recursive_merge_sort(array, helper_arr, low, high):
        """Recursively merge sort array, with sub-array to sort specified by
        starting (low) and ending (high) indices.

        Parameters
        ----------
        array : list
            Array to sort. Can be any comparable Python data type.
        helper_arr : list
            Array used to store values while merging
        low : int
            Index in array where sub-array starts
        high : int
            Index in array where sub-array ends

        Returns
        -------
        array : list
            Input (sub-) array sorted
        """
        # Check that low index is smaller than high index, and that they are
        # not equal (i.e. sub-array with 0 elements)
        # Stopping case for recursion
        if low < high:
            # Gnerate mid index, used to split sub-array (defined by low and
            # high) in two
            mid = int((high + low) / 2.0)
            # Recursively merge sort left half of split sub-array
            array = recursive_merge_sort(array, helper_arr, low, mid)
            # Recursively merge sort right half of split sub-array
            array = recursive_merge_sort(array, helper_arr, mid + 1, high)
            # Merge two split sub-arrays

            array = merge(array, helper_arr, low, mid, high)

        return array

    def merge(array, helper_arr, low, mid, high):
        """Merge sub-arrays within array, where low, mid and high define
        sub-arrays.

        Parameters
        ----------
        array : list
            Array to sort. Can be any comparable Python data type.
        helper_arr : list
            Array used to store values while merging
        low : int
            Index in array where first sub-array starts
        mid : int
            Index in array where first sub-array ends and second sub-array
            starts
        high : int
            Index in array where first sub-array ends

        Returns
        -------
        array : list
            Input (sub-) array merged (in order)
        """
        # Fill helper_arr with both sub-arrays
        helper_arr[low: high + 1] = array[low: high + 1].copy()

        # Set indexes of start of each sub-array in helper_arr, using these as
        # pointers to positions within the left and right sub-arrays
        helper_left = low
        helper_right = mid + 1
        # Use current as a pointer to position in array
        current = low

        # Iterate through helper array, using helper_left and helper_right
        # pointers
        while helper_left <= mid and helper_right <= high:
            # Compare leftmost element in both sub-arrays, that hasn't been
            # placed into array, keeping track using helper_left and
            # helper_right pointers, placing smaller of two in the array. Bear
            # in mind that both sub-arrays
            # are sorted.
            if helper_arr[helper_left] <= helper_arr[helper_right]:
                # i.e. element in left sub-array is smaller
                array[current] = helper_arr[helper_left]
                helper_left += 1
            else:
                # i.e. element in right sub-array is smaller
                array[current] = helper_arr[helper_right]
                helper_right += 1

            # Iterate pointer to position in array
            current += 1

        # Copy remaining elements in left sub-array into main-array
        # Don't need to copy elements in right array over because they are
        # already present (in order) in array. Only one of left or right
        # sub-arrays will have 'un-copied' elements, not both.
        remaining = mid - helper_left
        array[current: current + remaining + 1] = (
            helper_arr[helper_left: helper_left + remaining + 1].copy()
        )

        return array

    # Create copy to avoid modifying array inplace
    array = array.copy()

    # Initialise helper array, used to store elements of two arrays being
    # merged, while they are being inserted (in order) into main array
    helper_arr = [None] * len(array)

    # Perform merge sort recursively
    array = recursive_merge_sort(array, helper_arr, 0, len(array) - 1)

    if ascending:
        return array
    else:
        # Reverse array for descending order sort
        return array[::-1]


def quick_sort(array, ascending=True):
    """Sort array using quick sort algorithm.

    Parameters
    ----------
    array : list
        List to be sorted; Can contain any Python objects that can be compared
    ascending : bool, optional
        If True sort array from smallest to largest; False -> sort array from
        largest to smallest

    Returns
    -------
    list
        Input array sorted.
    """

    def recursive_quick_sort(array, left_index, right_index):
        """Recursively quick sort array, with sub-array to sort specified by
        starting (left) and ending (right) indices.

        Parameters
        ----------
        array : list
            Array to sort. Can be any comparable Python data type.
        left_index : int
            Index in array where sub-array starts
        right_index : int
            Index in array where sub-array ends

        Returns
        -------
        array : list
            Input (sub-) array sorted
        """

        # Partition sub-array
        array, index = partition(array, left_index, right_index)

        # Recursively quick sort left half of sub-array (to left of partition
        # element), provided that left_index pointer moves forward by at least
        # 2 places in partition function (i.e. needs sorting, more than 2
        # elements)
        # Stopping case for recursion
        if left_index < index - 1:
            array = recursive_quick_sort(array, left_index, index - 1)

        # Similar for right half
        # Stopping case for recursion
        if index < right_index:
            array = recursive_quick_sort(array, index, right_index)

        return array

    def partition(array, left_index, right_index):
        """Partition sub-array down middle, ensuring that all elements to left
        of partition element are smaller than it, and all elements to right
        are larger. Sub-array defined between left_index and right_index
        pointers.

        Parameters
        ----------
        array : list
            Array to sort. Can be any comparable Python data type.
        left_index : int
            Index in array where sub-array starts
        right_index : int
            Index in array where sub-array ends

        Returns
        -------
        array : list
            Input (sub-) array partitioned
        left_index : int
            Result value of left_index after performing partitioning
        """
        # Choose pivot point (halfway through sub-array)
        pivot_index = int((left_index + right_index) / 2.0)
        pivot_val = array[pivot_index]

        # Keep going through sub-array until left_index and right_index
        # pointers reach each other
        while left_index <= right_index:

            # Find leftmost element on the left of the partition that should be
            # on right side
            while array[left_index] < pivot_val:
                left_index += 1

            # Find rightmost element on the right of the partition that should
            # be on left side
            while array[right_index] > pivot_val:
                right_index -= 1

            # Swap elements on left and right sides that are out of place
            if left_index <= right_index:
                # Perform swap
                temp = array[right_index]
                array[right_index] = array[left_index]
                array[left_index] = temp

                # Iterate left_index and right_index pointers
                left_index += 1
                right_index -= 1

        return array, left_index

    # Create copy to avoid modifying array inplace
    array = array.copy()

    # Perform quick sort recursively
    array = recursive_quick_sort(array, 0, len(array) - 1)

    if ascending:
        return array
    else:
        # Reverse array for descending order sort
        return array[::-1]


def counting_sort(array, k, key_func=lambda x: x, ascending=True):
    """Sort array using counting sort algorithm.

    Parameters
    ----------
    array : list
        List to be sorted; Must produce integer values in the range 0 to k-1
        when key_func is applied to its elements
    k : int
        Max value of key_func(i), -1, where i an element of array
    key_func : func, optional
        Function to apply to elements of array to produce an integer in range 0
        to k-1
    ascending : bool, optional
        If True sort array from smallest to largest; False -> sort array from
        largest to smallest

    Returns
    -------
    output_arr : list
        Input array sorted.
    """
    # Create copy to avoid modifying array inplace
    array = array.copy()

    # Generate array to contain counts of each distinct value in array
    counts = [0] * k

    # Populate counts array by running through array
    for item in array:
        counts[key_func(item)] += 1

    # Calculate starting index for each k value, putting them in counts
    # Effectively storing number of items with key_func(item) less than i
    total = 0
    for i in range(k):
        old_count = counts[i]
        counts[i] = total
        total += old_count

    # Transfer to output array
    output_arr = [None] * len(array)
    for item in array:
        # Store item in correct position in array
        output_arr[counts[key_func(item)]] = item
        # Increment index for relevant k value
        counts[key_func(item)] += 1

    if ascending:
        return output_arr
    else:
        # Reverse array for descending order sort
        return output_arr[::-1]


def radix_sort(array, base=10, ascending=True, validate_dtype=False):
        """Sort array of integers using radix sort algorithm.

        Parameters
        ----------
        array : list of int
            List to be sorted
        base : int, optional
            Base to use for radix sort (higher base -> lower time complexity,
            higher space complexity)
        ascending : bool, optional
            If True sort array from smallest to largest; False -> sort array
            from largest to smallest

        Returns
        -------
        array : list
            Input array sorted.
        """

        def ensure_arr_of_ints(array):
            """Raise error if any elements in array aren't of int data type.

            Parameters
            array : list
                Array to check
            """
            for item in array:
                if type(item) != int:
                    raise Exception(
                        """radix_sort only supports int data type within array.
                         {} data is not supported""".format(
                            str(type(item))
                        ).replace('  ', '')
                    )

        # Create copy to avoid modifying array inplace
        array = array.copy()

        if validate_dtype:
            ensure_arr_of_ints(array)

        iteration_count = 0
        max_val = max(array)
        # Keep iterating until all digits have been used in the sort
        while max_val >= base**iteration_count:

            # Define function to extract correct digit from element in array
            def key_func(x): return int((x / base**iteration_count) % base)

            # Sort array using counting sort, where keys are iteration_count
            # digits from least significant digit of number
            array = counting_sort(array, base, key_func=key_func)

            iteration_count += 1

        if ascending:
            return array
        else:
            # Reverse array for descending order sort
            return array[::-1]


if __name__ == '__main__':

    arr = [7, 1, 5, 0, 10, 10, 1, 100, 115, 56]
    print('arr:', arr)

    # Bubble sort
    print(
        'arr sorted using bubble sort (ascending order):',
        bubble_sort(arr)
    )
    print(
        'arr sorted using bubble sort (descending order):',
        bubble_sort(arr, ascending=False)
    )

    # Selection sort
    print(
        'arr sorted using selection sort (ascending order):',
        selection_sort(arr)
    )
    print(
        'arr sorted using selection sort (descending order):',
        selection_sort(arr, ascending=False)
    )

    # Merge sort
    print(
        'arr sorted using merge sort (ascending order):',
        merge_sort(arr)
    )
    print(
        'arr sorted using merge sort (descending order):',
        merge_sort(arr, ascending=False)
    )

    # Quick sort
    print(
        'arr sorted using quick sort (ascending order):',
        quick_sort(arr)
    )
    print(
        'arr sorted using quick sort (descending order):',
        quick_sort(arr, ascending=False)
    )

    # Counting sort
    print(
        'arr sorted using counting sort (ascending order):',
        counting_sort(arr, max(arr) + 1)
    )
    print(
        'arr sorted using counting sort (descending order):',
        counting_sort(arr, max(arr) + 1, ascending=False)
    )

    # Radix sort
    print(
        'arr sorted using radix sort (ascending order):',
        radix_sort(arr)
    )
    print(
        'arr sorted using radix sort (descending order):',
        radix_sort(arr, ascending=False)
    )
