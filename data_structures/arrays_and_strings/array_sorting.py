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

    # Initialise helper array, used to store elements of two arrays being
    # merged, while they are being inserted (in order) into main array
    helper_arr = [None] * len(array)

    # Perform merge sort recursively
    return recursive_merge_sort(array, helper_arr, 0, len(array) - 1)

    def recursive_merge_sort(array, helper_arr, low, high):
        """
        """
        pass
        # need to return array

    def merge(array, helper_arr, low, mid, high):
        pass
        # need to return array




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

    # For merge sert, time it with different lists to check O(n) time is correct
