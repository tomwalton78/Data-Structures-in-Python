# Define the allowed characters for the trie. Currently set to use case
# insensitive english language characters.
ENGLISH_ALPHABET = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]


class Node():
    """Represent a single node within a Trie data structure.
    """

    def __init__(self, value, alphabet=ENGLISH_ALPHABET):
        """Initialse Node object with its value, and set up pointers to its
        child nodes.

        Parameters
        ----------
        value : any in alphabet
            Value of node. Can be any of the elements in alphabet.
        alphabet : list of str, optional
            List of allowed values Node can store.
        """

        self.is_end_of_string = False
        self.value = value
        self.children = [None] * len(alphabet)


class Trie():
    """Class to represent a trie data structure.
    """

    def _generate_alphabet_mapping(self):
        """Create dictionary that maps from characters in alphabet of Trie to
        its index in the children lists within each node.

        Returns
        -------
        dict
            chars in self.alphabet : corresponding index in Node's children
            list
        """
        return dict((k, v) for v, k in enumerate(self.alphabet))

    def __init__(self, alphabet=ENGLISH_ALPHABET):
        """Initialse Trie by defining root Node and storing mapping from chars
        in alphabet to corresponding index.

        Parameters
        ----------
        alphabet : list of str, optional
            List of char values that can be stored in Trie.
        """

        # Create root node
        self.root = Node("", alphabet=alphabet)

        self.alphabet = alphabet
        self.alphabet_mapping = self._generate_alphabet_mapping()

    def _insert_char(self, char, current_node):
        """Insert single char into Trie, as a child of current_node

        Parameters
        ----------
        char : str
            Character to insert
        current_node : Node
            Node of last char in sequence (parent node)

        Returns
        -------
        Node
            Child node corresponding to inserted char
        """
        # Retrieve index
        index = self.alphabet_mapping[char]

        # Initialise child node if not present
        if current_node.children[index] is None:
            current_node.children[index] = char

        # Return appropriate child node
        return current_node.children[index]

        def _insert_char_by_char(self, input_str):
            """Insert input_str one character at a time into Trie

            Parameters
            ----------
            input_str : str
                String to insert into Trie. All characters must be in defined
                alphabet.
            """
            # Start at root node
            current_node = self.root

            for char in input_str:

                current_node = _insert_char(char, current_node)

            # Ensure node for last char in input_str is flagged as the end of a
            # word
            current_node.is_end_of_string = True

    def _validate_str_type(self, input_str):
        """Raise error if input_str is not of type: str

        Parameters
        ----------
        input_str : any
            Object to check
        """
        if type(input_str) != str:
            raise TypeError("Invalid type, must be of type: str")

    def _validate_str_len(self, input_str):
        """Raise error if input_str is empty

        Parameters
        ----------
        input_str : str
            String to check
        """

    def insert(self, input_str):
        """Insert a string into the Trie.

        Parameters
        ----------
        input_str : str
            String to insert into Trie. All characters must be in defined
            alphabet.
        """
        # Validate input
        _validate_str_type(input_str)
        _validate_str_len(input_str)

        # Perform insert
        _insert_char_by_char(input_str)

    def _check_contains_char(self, char, current_node):
        """Check single char is in Trie, given that it should be a child of
        current_node

        Parameters
        ----------
        char : str
            Character to check
        current_node : Node
            Node of last char in sequence (parent node)

        Returns
        -------
        bool
            True if char is present as child of current_node in Trie, False
            otherwise
        Node
            Child node corresponding to checked char
        """
        # Retrieve index
        index = self.alphabet_mapping[char]

        # Check that child node is present
        if current_node.children[index] is None:
            return False, None
        else:
            # Return response & appropriate child node
            return True, current_node.children[index]

    def _check_contains_char_by_char(self, search_str):
        """Check that search_str is in Trie, one character at a time

        Parameters
        ----------
        search_str : str
            String to check for in Trie. All characters must be in defined
            alphabet.

        Returns
        -------
        bool
            True if search_str is present in Trie, False otherwise
        """
        # Start at root node
        current_node = self.root

        for char in search_str:

            char_present, current_node = _check_contains_char(
                char, current_node
            )

            if not char_present:
                return False

        # Check that node for last char in search_str is flagged as the end of
        # a word
        if current_node.is_end_of_string:
            return True
        else:
            return False

    def contains(self, search_str):
        """Search Trie for search_str, giving boolean response.

        Parameters
        ----------
        search_str : str
            String to search for in Trie

        Returns
        -------
        bool
            True if search_str is in Trie, False otherwise
        """
        # Validate input
        _validate_str_type(search_str)
        _validate_str_len(search_str)

        # Perform check
        return _check_contains_char_by_char(search_str)

    def _check_prefix_char_by_char(self, prefix_str):
        """Check that prefix_str is in Trie, one character at a time.

        Doesn't matter if prefix_str is a complete word, or a substring within
        another word.

        Parameters
        ----------
        prefix_str : str
            String to check for in Trie. All characters must be in defined
            alphabet.

        Returns
        -------
        bool
            True if prefix_str is present in Trie, False otherwise
        """
        # Start at root node
        current_node = self.root

        for char in prefix_str:

            char_present, current_node = _check_contains_char(
                char, current_node
            )

            if not char_present:
                return False

        return True

    def is_prefix(self, prefix_str):
        """Check if prefix_str is a valid prefix for the words in Trie.

        Parameters
        ----------
        prefix_str : str
            Prefix to check

        Returns
        -------
        bool
            True if prefix_str is a valid prefix, False otherwise
        """
        # Validate input
        _validate_str_type(prefix_str)
        _validate_str_len(prefix_str)

        # Perform check
        return _check_prefix_char_by_char(prefix_str)

    def delete(self, del_str, check_contains=True):
        """Delete del_str from Trie

        Parameters
        ----------
        del_str : str
            String to delete from Trie
        check_contains : bool
            Set flag to True to first check that Trie contains del_str, before
            attempting to delete it
        """
        # Validate input
        _validate_str_type(del_str)
        _validate_str_len(del_str)

        # Handle Trie not containing del_str
        if check_contains:
            if not contains(del_str):
                raise Exception(
                    "'{}' is not present within Trie; cannot delete it".format(
                        del_str
                    )
                )
        # Method:
        # Go through chars of word until you find node with no children, or
        # with is_end_of_string set to True (and word found matches del_str),
        # whichever comes first

        # Then, either set is_end_of_string flag to False if further child
        # nodes below, or, if no child nodes, simply cut off that node (will
        # create isolated chain of nodes further down that can't be accessed
        # (no pointers to the group, so will be garbage collected at some
        # point)

    def __str__(self):
        """Overload __str__ method to print all words within Trie

        Returns
        -------
        str
            Comma separated string of all words in Trie
        """
