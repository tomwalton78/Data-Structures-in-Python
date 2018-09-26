from data_structures.stacks_and_queues.queue import Queue


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
    """Represents an undirected (two-way) graph, stored using a list of node
    ids, each having pointers to its neighbours.
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
        """Connect 2 nodes in graph; bidirectional connection, since within an
        undirected graph.

        Parameters
        ----------
        id_1 : str
            Identifier for node 1
        id_2 : str
            Identifier for node 2
        """
        # Add neighbour to node 1
        self.nodes[id_1].neighbour_ids.append(id_2)
        # Add neighbour to node 2
        self.nodes[id_2].neighbour_ids.append(id_1)

    def disconnect(self, id_1, id_2):
        """Remove connection between 2 nodes in graph

        Parameters
        ----------
        id_1 : str
            Identifier for node 1
        id_2 : str
            Identifier for node 2
        """
        # Remove neighbour from node 1
        self.nodes[id_1].neighbour_ids.remove(id_2)
        # Remove neighbour from node 2
        self.nodes[id_2].neighbour_ids.remove(id_1)

    def delete(self, id):
        """Delete node from graph, along with all of its connections

        Parameters
        ----------
        id : str
            Identifier for node to delete
        """
        # Remove connections from neighbours to node that is being deleted
        for neigbour_id in self.nodes[id].neighbour_ids:
            self.nodes[neigbour_id].neighbour_ids.remove(id)

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

    def _has_path_dfs(self, visited, current_node_id, target_id):
        """Recursively search Graph looking for target_id, starting at a given
        node, using depth first search.

        Parameters
        ----------
        visited : dict
            Contains mapping from ids to bool indicating if they have been
            visited (True) or not (False). Format:
                id : Node
        current_node_id : str
            Id of current node  being examined
        target_id : str
            Id of target node that is being searched for

        Returns
        -------
        bool
            True if target_id found, False otherwise
        """

        # Retrieve current node
        current_node = self.nodes[current_node_id]

        # Check that current_node has not been visited before
        if visited[current_node.id]:
            return False

        # Check to see if current_node id matches the target node id
        if current_node.id == target_id:
            return True

        # Mark current_node as visited
        visited[current_node.id] = True

        # Check all neighbour nodes
        for neighbour_id in current_node.neighbour_ids:
            if self._has_path_dfs(visited, neighbour_id, target_id):
                return True

        # If no match found after search completes, return False
        return False

    def _has_path_bfs(self, visited, start_id, target_id):
        """Search Graph looking for node with target_id, starting at a given
        node (id_1), using breadth first search.

        Parameters
        ----------
        visited : dict
            Contains mapping from ids to bool indicating if they have been
            visited (True) or not (False). Format:
                id : Node
        start_id : str
            Id of node where search starts
        target_id : str
            Id of target node that is being searched for

        Returns
        -------
        bool
            True if target_id found, False otherwise
        """
        # Use Queue to store ids of nodes to be visited next
        nodes_to_visit = Queue()

        # Mark starting node as visited and add to Queue
        visited[start_id] = True
        nodes_to_visit.add(start_id)

        # Keep visiting nodes until none left to visit (Queue empty)
        while not nodes_to_visit.is_empty():

            # Extract node at front of Queue
            current_node_id = nodes_to_visit.remove()
            current_node = self.nodes[current_node_id]

            # Check to see if current node id matches target_id
            if current_node_id == target_id:
                return True

            # Check through current_node's neighbours
            for node_id in current_node.neighbour_ids:

                # Ensure node not already visited
                if not visited[node_id]:

                    # Mark node as visited and add to Queue
                    visited[node_id] = True
                    nodes_to_visit.add(node_id)

        # If no match found after search completes, return False
        return False

    def is_connected(self, id_1, id_2, method='BFS'):
        """Check whether there is a connection between 2 nodes, using specified
        search method.

        Parameters
        ----------
        id_1 : str
            Identifier for node 1
        id_2 : str
            Identifier for node 2
        method : str, optional
            Method to use for searching the graph. Possible values:
            "BFS" -> breadth first search
            "DFS" -> depth first search
        """

        # Generate dictionary to track which nodes have been visited
        visited = {k: False for k in self.nodes.keys()}

        if method == 'DFS':
            return self._has_path_dfs(visited, id_1, id_2)
        elif method == 'BFS':
            return self._has_path_bfs(visited, id_1, id_2)
        else:
            raise Exception(
                'Invalid value for method parameter: {}'.format(str(method))
            )


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

    print(
        'Using depth first search. Is "A" connected to "C"?',
        G.is_connected('A', 'C', method='DFS')
    )
    G.insert('X', 24)
    print(
        'Using depth first search. Is "A" connected to "X"?',
        G.is_connected('A', 'X', method='DFS')
    )

    print(
        'Using breadth first search. Is "A" connected to "C"?',
        G.is_connected('A', 'C', method='BFS')
    )
    print(
        'Using breadth first search. Is "A" connected to "X"?',
        G.is_connected('A', 'X', method='BFS')
    )
