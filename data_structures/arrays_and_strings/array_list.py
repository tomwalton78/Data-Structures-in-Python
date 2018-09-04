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

    def _expand_list(self):
        """Expand list by resizing_factor

        E.g. For resizing_factor of 2, a list of length 10 will become a list
        of length 20
        """

        # Compute how much to extend underlying list by
        new_length = self.resizing_factor * len(self.main_list)
        change_in_length = new_length - len(self.main_list)

        # Entend underlying list
        self.main_list = self.main_list.extend([None] * change_in_length)

    def append(self):
        pass

    def extend(self):
        pass

    def to_list(self):
        """Returns object contents, in form of standard Python list.
        """
        pass

    def __str__(self):
        pass

    def __iter__(self):
        pass
