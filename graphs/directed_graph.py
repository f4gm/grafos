class DirectedGraph:
    def __init__(self):
        self.vertices = []
        self.matrix = []

    def add_vertex(self, vertex):
        if vertex in self.vertices:
            return
        self.vertices.append(vertex)
        for row in self.matrix:
            row.append(None)
        self.matrix.append([None] * len(self.vertices))

    def add_edge(self, source, target, weight):
        self.add_vertex(source)
        self.add_vertex(target)
        row = self.vertices.index(source)
        column = self.vertices.index(target)
        self.matrix[row][column] = weight

    def get_vertices(self):
        return list(self.vertices)

    def get_neighbors(self, vertex):
        row = self.vertices.index(vertex)
        neighbors = []
        for column in range(len(self.vertices)):
            if self.matrix[row][column] is not None:
                neighbors.append(self.vertices[column])
        return neighbors
