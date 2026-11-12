import csv

from graphs.directed_graph import DirectedGraph
from graphs.undirected_graph import UndirectedGraph


def load_graph_from_file(file_path, directed=False):
    """
    Read a CSV file with the header source,target,weight and return a graph (workshop point 5).

    Returns an UndirectedGraph by default, or a DirectedGraph if directed=True.
    """
    if directed:
        graph = DirectedGraph()
    else:
        graph = UndirectedGraph()

    with open(file_path) as file:
        reader = csv.DictReader(file)
        for row in reader:
            graph.add_edge(row["source"], row["target"], int(row["weight"]))

    return graph
