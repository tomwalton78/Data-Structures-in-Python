class ArrayList():
    """This class implements a dynamically resizing array, with only some of
    the features of Python's built-in list.

    Built for educational purposes. Uses Python's built-in list under the hood.
    Idea is to practice creating a dynamically resizing array, treating
    Python's list object as if it were of a fixed size, and building
    'functionality' on top of it.
    """

    def __init__(self, initial_length=2, resizing_factor=2):
        """Initialise object with empty list, with initial length as specified.

        Parameters
        ----------
        initial_length : int, optional
            Starting length of underlying list
        resizing_factor : int, optional
            Factor by which to multiple underlying list length when list needs
            resizing
        """

        # Initialise underlying list, with no elements
        self.main_list = [None] * initial_length

        # Initialise variable to store number of elements inserted into
        # main_list, which will always be less than or equal to list length
        self.num_elements = 0

        self.resizing_factor = resizing_factor

    def _expand_main_list(self):
        """Expand list by resizing_factor

        E.g. For resizing_factor of 2, a list of length 10 will become a list
        of length 20
        """

        # Compute how much to extend underlying list by
        new_length = self.resizing_factor * len(self.main_list)
        change_in_length = new_length - len(self.main_list)

        # Entend underlying list
        self.main_list.extend([None] * change_in_length)

    def append(self, data):
        """Add single data element to main_list, increasing its size if
        necessary.
        Operates inplace.

        Parameters
        ----------
        data : any
            Item to append to main_list
        """
        # Check to see if main_list is full
        if self.num_elements == len(self.main_list):
            # Increase size of main_list
            self._expand_main_list()

        # Add element to mains_list
        self.main_list[self.num_elements] = data

        # Increment num elements counter
        self.num_elements += 1

    def extend(self, extension):
        """Append extension values to main_list. Wraps this object's append
        method.
        Parameters
        ----------
        extension : list
            List of Python objects to append to main_list
        """
        for element in extension:
            self.append(element)

    def to_list(self):
        """Returns object contents, in form of standard Python list.

        Returns
        -------
        list
            Values in main_list, converted to a standard Python list object
        """
        return self.main_list[:self.num_elements]

    def __str__(self):
        """Overload __str__ to print a more useful output: the values in
        main_list. Wraps this object's to_list method.

        Returns
        -------
        str
            Values in main_list, converted to a standard Python list object,
            then whole list converted to a str
        """
        return str(self.to_list())

    def __iter__(self):
        """Overload __iter__ to allow object to become iterable; allows
        iterating over values in main_list.

        Returns
        -------
        list_iterator
            Iterator object over values in main_list
        """
        return iter(self.to_list())


if __name__ == '__main__':

    a = ArrayList()

    a.append(3)
    a.extend([4, 5, 6, 7])
    a.append(8)

    print(a.to_list())
    print(a)

    for item in a:
        print(item)
