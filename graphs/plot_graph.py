import networkx as nx
import matplotlib.pyplot as plt

def plot_graph(graph):
    """
    Plot a directed or undirected graph using NetworkX and Matplotlib.

    Args:
        graph: An instance of DirectedGraph or UndirectedGraph.
    """

    # Determine the graph type and create the corresponding NetworkX graph.
    if hasattr(graph, "matrix") and hasattr(graph, "vertices"):
        # Directed graph represented by an adjacency matrix.
        G = nx.DiGraph()

        G.add_nodes_from(graph.vertices)

        for i, source in enumerate(graph.vertices):
            for j, target in enumerate(graph.vertices):
                weight = graph.matrix[i][j]

                if weight is not None:
                    G.add_edge(source, target, weight=weight)

    elif hasattr(graph, "adjacency_list"):
        # Undirected graph represented by an adjacency list.
        G = nx.Graph()

        for vertex, neighbors in graph.adjacency_list.items():
            G.add_node(vertex)

            for neighbor, weight in neighbors.items():
                G.add_edge(vertex, neighbor, weight=weight)

    else:
        raise TypeError("Unsupported graph type.")

    # Calculate node positions.
    pos = nx.spring_layout(G, seed=42)

    # Draw the graph.
    plt.figure(figsize=(9, 6))

    nx.draw_networkx(
        G,
        pos,
        with_labels=True,
        node_color="lightblue",
        node_size=800,
        font_size=11,
        font_weight="bold",
        edge_color="gray",
        arrows=True,
        arrowsize=20
    )

    # Display edge weights.
    edge_labels = nx.get_edge_attributes(G, "weight")

    if edge_labels:
        nx.draw_networkx_edge_labels(
            G,
            pos,
            edge_labels=edge_labels,
            font_size=10
        )

    plt.title("Graph Visualization")
    plt.axis("off")
    plt.tight_layout()
    plt.show()
