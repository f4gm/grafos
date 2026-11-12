from typing import cast

from graphs.graph_loader import load_graph_from_file
from graphs.undirected_graph import UndirectedGraph
from graphs.directed_graph import DirectedGraph

filename = "csv\\ejemplo_1.csv"

undirected_graph = cast(
  UndirectedGraph,
  load_graph_from_file(filename, False)
)
directed_graph = cast(
  DirectedGraph,
  load_graph_from_file(filename, True)
)

undirected_graph.is_connected()
undirected_graph.has_cycle()
undirected_graph.is_tree()
undirected_graph.is_forest()