class DirectedGraph:
    """
    Directed graph (workshop point 4). Uses an adjacency matrix: matrix[row][column]
    is the weight of the edge row -> column, or None if there is no edge.
    """

    def __init__(self):
        """Create an empty graph."""
        self.vertices = []
        self.matrix = []
        self.vertices_number = 0
        self.edges_number = 0

    def add_vertex(self, vertex):
        """Add a vertex to the list and grow the matrix by one row and one column."""
        if vertex in self.vertices:
            return
        self.vertices.append(vertex)
        self.vertices_number += 1
        for row in self.matrix:
            row.append(None)
        self.matrix.append([None] * len(self.vertices))

    def add_edge(self, source, target, weight):
        """Add a directed edge from source to target."""
        self.add_vertex(source)
        self.add_vertex(target)
        row = self.vertices.index(source)
        column = self.vertices.index(target)
        if self.matrix[row][column] is None:
            self.edges_number += 1
        self.matrix[row][column] = weight

    def get_vertices(self):
        """Return the list of vertices."""
        return list(self.vertices)

    def get_neighbors(self, vertex):
        """Return the vertices that can be reached directly from vertex."""
        row = self.vertices.index(vertex)
        neighbors = []
        for column in range(len(self.vertices)):
            if self.matrix[row][column] is not None:
                neighbors.append(self.vertices[column])
        return neighbors
