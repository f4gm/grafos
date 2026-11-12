class UndirectedGraph:
    """Undirected graph (workshop point 3). Uses an adjacency list: {vertex: {neighbor: weight}}."""

    def __init__(self):
        """Create an empty graph."""
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        """Add a vertex if it does not exist yet."""
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = {}

    def add_edge(self, source, target, weight):
        """Add an edge between source and target, stored in both directions."""
        self.add_vertex(source)
        self.add_vertex(target)
        self.adjacency_list[source][target] = weight
        self.adjacency_list[target][source] = weight

    def get_vertices(self):
        """Return the list of vertices."""
        return list(self.adjacency_list)

    def get_neighbors(self, vertex):
        """Return the list of neighbors of a vertex."""
        return list(self.adjacency_list[vertex])
