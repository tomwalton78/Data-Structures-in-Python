class StringBuilder():
    """This class implements a string like object, which is actually a list of
    strings, which are only concatenated into a single string when required,
    for efficiency reasons.
    """

    def __init__(self):
        """Intialise empty list, to store strings
        """
        self.string_list = []

    def append(self, *args):
        """Append input strings to object's list of strings (string_list)

        Parameters
        ----------
        *args : str
            Variable amount of strings to append
        """
        for string in args:
            self.string_list.append(string)

    def to_string(self):
        """Return list of strings as a single list

        Returns
        -------
        str
            Joined list of strings
        """

        return ''.join(self.string_list)

    def extend(self, list_of_strings):
        """Extend string_list with input list of strings
        """
        self.string_list.extend(list_of_strings)

    def __add__(self, input_strings):
        """Overload add operator. Append input strings and return StringBuilder
        object, with strings added. Does not add inplace.

        Parameters
        ----------
        input_strings : str or list of str
            Strings to append

        Returns
        -------
        temp_self : StringBuilder
            Copy of self, with input_args added
        """

        # Ensure input is list, to allow always using extend method on input
        if type(input_strings) != list:
            input_strings = [input_strings]

        # Create copy of self, to return
        current_string_list = self.string_list.copy()
        temp_self = StringBuilder()
        temp_self.extend(current_string_list)

        # Add input strings
        temp_self.extend(input_strings)

        return temp_self


if __name__ == '__main__':

    s = StringBuilder()

    s.append('Hello', ' ', 'world')
    s.extend(['.', ' ', 'Python!'])

    s2 = s + '--extension'

    print(s.to_string())

    print(s2.to_string())
