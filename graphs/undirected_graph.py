class UndirectedGraph:
    """
    Undirected graph (workshop point 3). Uses an adjacency list: {vertex: {neighbor: weight}}.
    """

    def __init__(self):
        """Create an empty graph."""
        self.adjacency_list = {}
        self.vertices_number = 0
        self.edges_number = 0

    def add_vertex(self, vertex):
        """Add a vertex if it does not exist yet."""
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = {}
            self.vertices_number+=1

    def add_edge(self, source, target, weight):
        """Add an edge between source and target, stored in both directions."""
        self.add_vertex(source)
        self.add_vertex(target)

        # Check whether the edge already exists.
        if target not in self.adjacency_list[source]:
            self.edges_number += 1

        self.adjacency_list[source][target] = weight
        self.adjacency_list[target][source] = weight

    def get_vertices(self):
        """Return the list of vertices."""
        return list(self.adjacency_list)

    def get_neighbors(self, vertex):
        """Return the list of neighbors of a vertex."""
        return list(self.adjacency_list[vertex])

    def dfs(self, start, parent=None):
        """Perform Depth-First Search starting from a given vertex."""
        visited = set()
        stack = [(start, parent)]
        traversal = []
        parents = {}

        while stack:
            current, current_parent = stack.pop()

            if current in visited:
                continue

            visited.add(current)
            traversal.append(current)
            parents[current] = current_parent

            for neighbor in self.get_neighbors(current):
                if neighbor not in visited:
                    stack.append((neighbor, current))

        return traversal, parents

    def is_connected(self, print_result: bool = True):
        """
        Determine whether the graph is connected or not. (workshop point 6)
        """
        result = True
        if self.vertices_number == 0:
            print(f"is_connected: {result}") if print_result else ...
            return result
        
        vertices = self.get_vertices()
        traversal, _ = self.dfs(start=vertices[0])
        
        # The graph is connected if every vertex was visited.
        result = len(traversal) == self.vertices_number
        print(f"is_connected: {result}") if print_result else ...
        return result

    def has_cycle(self, print_result: bool = True):
        """
        Determine whether the undirected graph contains a cycle. (workshop point 7)
        """
        result = True

        visited = set()

        for vertex in self.get_vertices():

            if vertex not in visited:
                traversal, parents = self.dfs(vertex)

                # Store the vertices belonging to the current component.
                component = set(traversal)
                visited.update(component)

                for current in traversal:
                    for neighbor in self.get_neighbors(current):

                        # Tree edges (the parent and the DFS children)
                        # do not form a cycle.
                        if neighbor not in component:
                            continue
                        if neighbor == parents[current]:
                            continue
                        if parents.get(neighbor) == current:
                            continue

                        # Any other edge inside the component is a back
                        # edge, so the component contains a cycle.
                        print(f"has_cycle: {result}") if print_result else ...
                        return result
        
        result = False
        print(f"has_cycle: {result}") if print_result else ...
        return result

    def is_tree(self, print_result: bool = True):
        """Determine whether the graph is a tree. (workshop point 8)"""
        result = (
            self.is_connected(print_result=False) and
            not self.has_cycle(print_result=False) and
            self.edges_number == self.vertices_number - 1
        )
        print(f"is_tree: {result}") if print_result else ...
        return result

    def is_forest(self, print_result: bool = True):
        """Determine whether the graph is a forest. (workshop point 9)"""
        result = not self.has_cycle(print_result=False)
        print(f"is_forest: {result}") if print_result else ...
        return result