from collections import deque


def breadth_first_search(graph, start_node_name, end_node_name):
    closed_nodes = set()
    successors = {}
    prev_node = None
    open_nodes = deque([(start_node_name, prev_node)])
    while len(open_nodes) > 0:
        node_to_expand, prev_node = open_nodes.popleft()
        closed_nodes.add(node_to_expand)
        successors[node_to_expand] = prev_node
        if end_node_name in closed_nodes:
            path = get_path(end_node_name, successors)
            return path
        expand(graph, node_to_expand, closed_nodes, open_nodes)
    raise ValueError(f"No path found from start node {start_node_name} to end node {end_node_name} in graph")


def expand(graph, node_to_expand, closed_set, open_list):
    corner_nodes = graph.edges(node_to_expand)
    for corner_node in corner_nodes:
        if corner_node in closed_set:
            continue
        open_list.append((corner_node, node_to_expand))
    return closed_set


def get_path(end_node_name, successors):
    path_backwards = [end_node_name]
    current_node_name = end_node_name
    while successors[current_node_name] != None:
        current_node_name = successors[current_node_name]
        path_backwards.append(current_node_name)
    path = path_backwards[::-1]
    return path