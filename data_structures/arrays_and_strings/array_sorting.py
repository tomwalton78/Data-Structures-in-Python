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
    # Use swap_count to keep track of number of swaps on each sweep
    swap_count = 1

    # Keep sweeping through array until no swaps need to occur
    while swap_count > 0:

        # Reset swap scount at beginning of sweep
        swap_count = 0

        for i, j in enumerate(array.copy()[:-1]):

            # Swap pair of elements being compared if out of order
            if array[i] > array[i+1]:
                # Perform swap
                temp = array[i+1]
                array[i+1] = array[i]
                array[i] = temp

                # Increment swap count
                swap_count += 1

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
            #CHECK TO FIND WAY TO NOT NEED +1
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
        helper_arr[low: high + 1] = array[low: high + 1]

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
            if helper_arr[helper_left <= helper_arr[helper_right]]:
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
            helper_arr[helper_left: remaining + 1]
        )

        return array

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




if __name__ == '__main__':

    arr = [7, 1, 5, 9, 0, 10, 10, 1]
    print('arr:', arr)

    print(
        'arr sorted using bubble sort (ascending order):',
        bubble_sort(arr)
    )
    print(
        'arr sorted using bubble sort (descending order):',
        bubble_sort(arr, ascending=False)
    )

    print(
        'arr sorted using selection sort (ascending order):',
        selection_sort(arr)
    )
    print(
        'arr sorted using selection sort (descending order):',
        selection_sort(arr, ascending=False)
    )

    print(
        'arr sorted using merge sort (ascending order):',
        merge_sort(arr)
    )
    print(
        'arr sorted using merge sort (descending order):',
        merge_sort(arr, ascending=False)
    )

    # For merge sert, time it with different lists to check O(n) time is correct
