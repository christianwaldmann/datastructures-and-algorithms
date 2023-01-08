from graphs.dijkstra import dijkstra
from data_structures.graph import GraphAdjacencyMatrix


def test_dijkstra_returns_correct_result():
    graph = GraphAdjacencyMatrix()
    graph.add_node("A")
    graph.add_node("B")
    graph.add_node("C")
    graph.add_node("D")
    graph.add_node("E")
    graph.add_node("F")
    graph.add_edge("A", "B", value=2, bidirectional=True)
    graph.add_edge("A", "C", value=1, bidirectional=True)
    graph.add_edge("B", "C", value=4, bidirectional=True)
    graph.add_edge("B", "D", value=3, bidirectional=True)
    graph.add_edge("C", "E", value=2, bidirectional=True)
    graph.add_edge("D", "E", value=1, bidirectional=True)
    graph.add_edge("D", "F", value=2, bidirectional=True)
    graph.add_edge("E", "F", value=4, bidirectional=True)
    start_node_name = "A"
    end_node_name = "F"

    path = dijkstra(graph, start_node_name, end_node_name)

    assert path == ["A", "C", "E", "D", "F"]

