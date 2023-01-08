import heapq
from collections import deque


def dijkstra(graph, start_node_name, end_node_name):
    closed_nodes = set()
    successors = {}
    prev_node = None
    distances = {}
    open_nodes = [(0, start_node_name, prev_node)]
    while len(open_nodes) > 0:
        distance_to_start, node_to_expand, prev_node = heapq.heappop(open_nodes)
        if node_to_expand in closed_nodes:
            continue
        closed_nodes.add(node_to_expand)
        successors[node_to_expand] = prev_node
        distances[node_to_expand] = distance_to_start
        if end_node_name in closed_nodes:
            path = get_path(end_node_name, successors)
            return path
        expand(graph, node_to_expand, closed_nodes, open_nodes, distances)
    raise ValueError(f"No path found from start node {start_node_name} to end node {end_node_name} in graph")


def expand(graph, node_to_expand, closed_set, open_list, dist_to_start):
    corner_nodes = graph.edges(node_to_expand)
    node_to_expand_dist_to_start = dist_to_start[node_to_expand]
    for corner_node in corner_nodes:
        if corner_node in closed_set:
            continue
        dist_to_start = node_to_expand_dist_to_start + graph.get_edge(node_to_expand, corner_node)
        # Heap sorts tuples by default by the first element, so in this case the heap sorts by the distance to start
        heapq.heappush(open_list, (dist_to_start, corner_node, node_to_expand))
    return closed_set


def get_path(end_node_name, successors):
    path_backwards = [end_node_name]
    current_node_name = end_node_name
    while successors[current_node_name] != None:
        current_node_name = successors[current_node_name]
        path_backwards.append(current_node_name)
    path = path_backwards[::-1]
    return path