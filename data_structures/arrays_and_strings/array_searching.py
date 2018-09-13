from data_structures.arrays_and_strings.array_sorting import quick_sort


def binary_search(array, value):
    """Search for value in sorted array, using binary search

    Continually divide (sub-) array in half until value is found, or entire
    array has been searched. Iterative approach.

    Parameters
    array : list
        List to search. Must be sorted.
    value : any
        Value to search for. Must be same type as elements in array.

    Returns
    -------
    bool
        True if array contains value, False otherwise
    """
    # Set starting indexes, which will be used to index sub-array as it shrinks
    low = 0
    high = len(array) - 1

    # Keep searching until low and high pointers overlap
    while (high - low) > 0:

        mid = int((high + low) / 2)

        # Check to see if dividing index (mid) equals value we're searching for
        if array[mid] == value:
            return True

        elif value < array[mid]:
            # -1 since don't want to check value at mid again (redundant)
            high = array[mid] - 1

        elif value > array[mid]:
            # +1 since don't want to check value at mid again (redundant)
            low = array[mid] + 1

    return False


if __name__ == '__main__':

    arr = [7, 1, 5, 0, 10, 10, 1, 100, 115, 56, 9, 2, 7, 4, 2, 77, 59, 246]
    print('arr:', arr)

    sorted_arr = quick_sort(arr)
    print('sorted arr:', sorted_arr)

    print('7 is in sorted_arr:', binary_search(sorted_arr, 7))
    print('71 is in sorted_arr:', binary_search(sorted_arr, 71))
