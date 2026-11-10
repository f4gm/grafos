class UndirectedGraph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = {}

    def add_edge(self, source, target, weight):
        self.add_vertex(source)
        self.add_vertex(target)
        self.adjacency_list[source][target] = weight
        self.adjacency_list[target][source] = weight

    def get_vertices(self):
        return list(self.adjacency_list)

    def get_neighbors(self, vertex):
        return list(self.adjacency_list[vertex])
