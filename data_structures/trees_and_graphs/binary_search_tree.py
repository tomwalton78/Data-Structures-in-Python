class Node():

    def __init__(self, data, left_node=None, right_node=None):
        """Initialise Node object with a value (data) and references to the
        left and right nodes of this Node.

        Parameters
        ----------
        data
            Data to store in node. Can be any python object.
        left_node : Node, optional
            Reference to Node object on the left in tree
        right_node : Node, optional
            Reference to Node object on the right in tree
        """
        self.data = data
        self.left_node = left_node
        self.right_node = right_node


class BinarySearchTree():
    """Class to implement a binary search tree data structure.

    Tree is ordered such that left node is always less than the node above it,
    right node is greater than the node above it. No duplicate values allowed.
    """

    def __init__(self):
        """Initialise BinarySearchTree containing no data
        """
        self.root = None

    def _recursive_insert(self, current_node, data):
        """Try to insert data at either left or right node, if at
        end of tree branch, otherwise recursively walk through branches of
        tree.

        Parameters
        ----------
        data : any
            Data to insert. Can be any Python object
        """

        # Go to left node
        if data < current_node.data:
            # Create new leaf node if at end of tree
            if current_node.left_node is None:
                current_node.left_node = Node(data)
            # If not at end of tree, recursively walk through branches
            else:
                _recursive_insert(current_node.left_node, data)

        # Go to right node
        elif data > current_node.data:
            # Create new leaf node if at end of tree
            if current_node.right_node is None:
                current_node.right_node = Node(data)
            # If not at end of tree, recursively walk through branches
            else:
                _recursive_insert(current_node.right_node, data)

        # Handle duplicate values
        elif data == current_node.data:
            raise Exception('Cannot insert duplicate values into tree.)

    def insert(self, data):
        """Insert element into tree, keeping order.

        Parameters
        ----------
        data : any
            Data to insert. Can be any Python object
        """

        # Handle case of empty tree
        if self.root is None:
            self.root = Node(data)
            return

        # Recursively insert data, starting at root node
        _recursive_insert(self.root, data)

    def _recursive_find(self, current_node, value):
        """Try to find value at either left or right node, otherwise
        recursively walking through branches of tree if value not found.

        Parameters
        ----------
        value : any
            Value to look for. Can be any Python object
        """

        # Go to left node
        if value < current_node.data:
            # If at end of tree, value has not been found, return False
            if current_node.left_node is None:
                return False
            # If not at end of tree, recursively walk through branches
            else:
                return _recursive_find(current_node.left_node, value)

        # Go to right node
        elif value > current_node.data:
            # If at end of tree, value has not been found, return False
            if current_node.right_node is None:
                return False
            # If not at end of tree, recursively walk through branches
            else:
                return _recursive_find(current_node.right_node, value)

        # Check current node for value
        elif value == current_node.data:
            return True

    def contains(self, value):
        """Check if tree contains specified value, giving boolean response.

        Parameters
        ----------
        value : any
            Value to try to find in tree
        """

        # Handle case of empty tree
        if self.root is None:
            print('Value not found since tree is empty')
            return False

        # Check root node for value
        if self.root.data == value:
            return True

        # Recursively look for value, starting at root node
        return _recursive_find(self.root, value)
