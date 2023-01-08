from abc import ABC, abstractmethod
import numpy as np


class Graph(ABC):

    @abstractmethod
    def add_node(self, node):
        pass

    @abstractmethod
    def add_edge(self, start_node_name, end_node_name, value, bidirectional):
        pass

    @abstractmethod
    def get_edge(self, start_node_name, end_node_name):
        pass

    @abstractmethod
    def edges(self, node_name):
        pass

    @abstractmethod
    def incoming_edges(self, node_name):
        pass

    @abstractmethod
    def outgoing_edges(self, node_name):
        pass

    @abstractmethod
    def all_nodes(self):
        pass

    @abstractmethod
    def node_count(self):
        pass

    @abstractmethod
    def __str__(self):
        pass


class GraphAdjacencyMatrix(Graph):

    def __init__(self, size=1000):
        self.size = size
        self.data = -1 * np.ones(shape=(size, size))
        self.nodes = {}
        self.nodes_index = 0

    def add_node(self, node_name):
        self.nodes[node_name] = self.nodes_index
        self.nodes_index += 1

    def add_edge(self, start_node_name, end_node_name, value=1, bidirectional=False):
        start_node_index = self.nodes[start_node_name]
        end_node_index = self.nodes[end_node_name]
        self.data[start_node_index][end_node_index] = value
        if bidirectional:
            self.data[end_node_index][start_node_index] = value

    def get_edge(self, start_node_name, end_node_name):
        start_node_index = self.nodes[start_node_name]
        end_node_index = self.nodes[end_node_name]
        return self.data[start_node_index][end_node_index]

    def edges(self, node_name):
        return self.incoming_edges(node_name).union(self.outgoing_edges(node_name))

    def incoming_edges(self, node_name):
        incoming_edges = set()
        for start_node_name in self.all_nodes():
            if self.get_edge(start_node_name, node_name) != -1:
                incoming_edges.add(start_node_name)
        return incoming_edges

    def outgoing_edges(self, node_name):
        outgoing_edges = set()
        for end_node_name in self.all_nodes():
            if self.get_edge(node_name, end_node_name) != -1:
                outgoing_edges.add(end_node_name)
        return outgoing_edges

    def all_nodes(self):
        return list(self.nodes.keys())

    def node_count(self):
        return len(self.nodes.keys())

    def __str__(self):
        string = ""
        for i, start_node in zip(range(self.nodes_index), self.nodes.keys()):
            string += f"{start_node: <6}: "
            for j in range(self.nodes_index):
                string += f"{self.data[i][j]: <6}, "
            string += "\n"
        return string
