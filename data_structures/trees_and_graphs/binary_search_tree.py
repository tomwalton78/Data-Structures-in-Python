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
                self._recursive_insert(current_node.left_node, data)

        # Go to right node
        elif data > current_node.data:
            # Create new leaf node if at end of tree
            if current_node.right_node is None:
                current_node.right_node = Node(data)
            # If not at end of tree, recursively walk through branches
            else:
                self._recursive_insert(current_node.right_node, data)

        # Handle duplicate values
        elif data == current_node.data:
            raise Exception('Cannot insert duplicate values into tree.')

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
        self._recursive_insert(self.root, data)

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
                return self._recursive_find(current_node.left_node, value)

        # Go to right node
        elif value > current_node.data:
            # If at end of tree, value has not been found, return False
            if current_node.right_node is None:
                return False
            # If not at end of tree, recursively walk through branches
            else:
                return self._recursive_find(current_node.right_node, value)

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
        return self._recursive_find(self.root, value)

    def _display(self, node):
        """Print the data value of the input node

        Parameters
        ----------
        node : Node
            Node to display
        """
        print(node.data)

    def _recursive_in_order_traversal(
            self, current_node, node_func=_display
            ):
        """Recursively visit nodes, usng in order binary tree traversal.
        Parameters
        ----------
        current_node : Node
            Last node visited
        node_func : func
            Function to apply to each node
        """

        # Visit left node
        if current_node.left_node is not None:
            self._recursive_in_order_traversal(
                current_node.left_node, node_func=node_func
            )

        # Visit centre node
        node_func(current_node)

        # Visit right node
        if current_node.right_node is not None:
            self._recursive_in_order_traversal(
                current_node.right_node, node_func=node_func
            )

    def _recursive_pre_order_traversal(
            self, current_node, node_func=_display
            ):
        """Recursively visit nodes, usng pre-order binary tree traversal.
        Parameters
        ----------
        current_node : Node
            Last node visited
        node_func : func
            Function to apply to each node
        """

        # Visit centre node
        node_func(current_node)

        # Visit left node
        if current_node.left_node is not None:
            self._recursive_in_order_traversal(
                current_node.left_node, node_func=node_func
            )

        # Visit right node
        if current_node.right_node is not None:
            self._recursive_in_order_traversal(
                current_node.right_node, node_func=node_func
            )

    def _recursive_post_order_traversal(
            self, current_node, node_func=_display
            ):
        """Recursively visit nodes, usng post-order binary tree traversal.
        Parameters
        ----------
        current_node : Node
            Last node visited
        node_func : func
            Function to apply to each node
        """

        # Visit left node
        if current_node.left_node is not None:
            self._recursive_in_order_traversal(
                current_node.left_node, node_func=node_func
            )

        # Visit right node
        if current_node.right_node is not None:
            self._recursive_in_order_traversal(
                current_node.right_node, node_func=node_func
            )

        # Visit centre node
        node_func(current_node)

    def traverse(self, method='in-order', node_func=_display):
        """Traverse binary tree using specified recursive traversal function,
        applying node_func to each node that is touched.

        Parameters
        ----------
        method : str
            Type of traversal to use. Possible values:
                "in-order"
                "pre-order"
                "post-order"
        node_func : func, optional
            Function to apply to each node
        """

        # Handle case of empty tree
        if self.root is None:
            print('Tree is empty')
            return

        # Select apppropriate recursive traversal function
        mapping = {
            'in-order': self._recursive_in_order_traversal,
            'pre-order': self._recursive_pre_order_traversal,
            'post-order': self._recursive_post_order_traversal,
        }
        traverse_func = mapping[method]

        # Recursively traverse tree using specified traversal function,
        # starting at root node
        traverse_func(self.root, node_func=self._display)


if __name__ == '__main__':

    b = BinarySearchTree()

    b.traverse()

    [b.insert(i) for i in [6, 3, 5, 7, 1, 8, 4, 9]]

    print('Tree contains 7:', b.contains(7))
    print('Tree contains 100:', b.contains(100))

    print('\nIn-order traversal:')
    b.traverse(method='in-order')

    print('\nPre-order traversal:')
    b.traverse(method='pre-order')

    print('\nPost-order traversal:')
    b.traverse(method='post-order')
