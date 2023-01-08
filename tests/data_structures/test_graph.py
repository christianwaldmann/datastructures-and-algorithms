from data_structures.graph import GraphAdjacencyMatrix


def test_graph_adjacency_matrix_adding_nodes_and_edges_behaves_correctly():
    graph = GraphAdjacencyMatrix()
    graph.add_node("A")
    graph.add_node("B")
    graph.add_node("C")
    graph.add_edge("A", "B")
    graph.add_edge("B", "C")
    graph.add_edge("C", "A")
    assert graph.node_count() == 3
    assert graph.all_nodes() == ["A", "B", "C"]
    assert graph.get_edge("A", "B") == 1
    assert graph.get_edge("B", "C") == 1
    assert graph.get_edge("C", "A") == 1
    assert graph.get_edge("B", "A") == -1
    assert graph.get_edge("C", "B") == -1
    assert graph.get_edge("A", "C") == -1
    assert graph.get_edge("A", "A") == -1
    assert graph.get_edge("B", "B") == -1
    assert graph.get_edge("C", "C") == -1
    assert graph.outgoing_edges("A") == {"B"}
    assert graph.outgoing_edges("B") == {"C"}
    assert graph.outgoing_edges("C") == {"A"}
    assert graph.incoming_edges("A") == {"C"}
    assert graph.incoming_edges("B") == {"A"}
    assert graph.incoming_edges("C") == {"B"}
    assert graph.edges("A") == {"B", "C"}
    assert graph.edges("B") == {"A", "C"}
    assert graph.edges("C") == {"A", "B"}

