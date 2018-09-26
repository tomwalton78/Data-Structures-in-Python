class Node():
    """Represents a single node/point within a graph
    """

    def __init__(self, id, value):
        """Initialise node with an id, value and empty list of neighbour ids
        (adjacency list).

        Parameters
        ----------
        id : str
            Identifier for node
        value : any
            Value of node, can be any Python object
        """
        self.id = id
        self.value = value
        self.neighbour_ids = []


class Graph():
    """Represents a directed (one-way) graph, stored using a list of node
    ids, each having references to its neighbours.
    """

    def __init__(self):
        """Initialise nodes list
        """
        # Hashmap for connecting node ids and Node objects
        self.nodes = {}

    def _check_id(self, id):
        """Checks that id isn't already stored, for avoiding overwriting
        existing ids.

        Parameters
        ----------
        id : str
            Identifier to check
        """
        if id in self.nodes:
            raise Exception("Id already stored in graph")

    def insert(self, id, value):
        """Insert node into graph

        Parameters
        ----------
        id : str
            Identifier for node
        value : any
            Value of node, can be any Python object
        """
        # Ensure id doesn't already exist in graph
        self._check_id(id)

        # Insert node into graph
        self.nodes[id] = Node(id, value)

    def connect(self, id_1, id_2):
        """Connect node with id 1 to node with id 2 in graph; unidrectional
        connection, since within a directed graph.

        Parameters
        ----------
        id_1 : str
            Identifier for node 1; source for connection
        id_2 : str
            Identifier for node 2; destination for connection
        """
        # Add neighbour to node 1
        self.nodes[id_1].neighbour_ids.append(id_2)

    def disconnect(self, id_1, id_2):
        """Remove connection between 2 nodes in graph

        Parameters
        ----------
        id_1 : str
            Identifier for node 1; source for connection
        id_2 : str
            Identifier for node 2; destination for connection
        """
        # Remove neighbour from node 1
        self.nodes[id_1].neighbour_ids.remove(id_2)

    def delete(self, id):
        """Delete node from graph, along with all of its connections

        Parameters
        ----------
        id : str
            Identifier for node to delete
        """
        # Search through all nodes, and remove any connections to node that is
        # being deleted
        for node_id, node in self.nodes.items():
            # Attempt to remove node
            try:
                node.neighbour_ids.remove(id)
            except ValueError:
                pass

        # Delete node itself
        self.nodes.pop(id, None)

    def __str__(self):
        """Overload __str__ method to return all nodes in graph, their values
        and their neighbours.

        Returns
        -------
        str
            String containing all nodes in graph, and details about them
        """
        # Extract and store info about each node as a string
        pretty_node_list = []
        for node_id, node in self.nodes.items():
            node_str = 'Id: {}, Value: {}, Neighbour ids: {}'.format(
                node.id, str(node.value), [str(i) for i in node.neighbour_ids]
            )
            pretty_node_list.append(node_str)

        return '\n'.join(pretty_node_list)


if __name__ == '__main__':

    G = Graph()

    G.insert('A', 1)
    G.insert('B', 2)
    G.insert('C', 3)
    G.insert('D', 4)
    G.insert('E', 5)

    print(G, '\n')

    G.connect('A', 'B')
    G.connect('A', 'C')
    G.connect('D', 'E')
    G.connect('C', 'E')
    G.connect('A', 'D')

    print(G, '\n')

    G.disconnect('A', 'D')

    print(G, '\n')

    G.delete('B')

    print(G, '\n')
