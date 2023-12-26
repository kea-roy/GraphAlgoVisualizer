import networkx as nx
from collections import deque


def get_dfs_color_maps(graph: nx.Graph, s_node: str) -> list[list[str]]:
    color_maps = []
    visited = []
    stack = deque()
    stack.append(s_node)
    while len(stack) > 0:
        cur_node = stack.pop()
        if cur_node in visited:
            continue
        visited.append(cur_node)
        # add neighbors to stack in reverse order
        temp_stack = deque()
        for neighbor in graph.neighbors(cur_node):
            temp_stack.append(neighbor)
        while len(temp_stack) > 0:
            stack.append(temp_stack.pop())
        # add new color_map to color_maps
        color_map = []
        for node in graph.nodes:
            if node in visited:
                color_map.append("green")
            else:
                color_map.append("steelblue")
        color_maps.append(color_map)
    return color_maps


def get_bfs_color_maps(graph: nx.Graph, s_node: str) -> list[list[str]]:
    color_maps = []
    visited = []
    queue = deque()
    queue.append(s_node)
    while len(queue) > 0:
        cur_node = queue.popleft()
        if cur_node in visited:
            continue
        visited.append(cur_node)
        # add neighbors to queue
        for neighbor in graph.neighbors(cur_node):
            queue.append(neighbor)
        # add new color_map to color_maps
        color_map = []
        for node in graph.nodes:
            if node in visited:
                color_map.append("green")
            else:
                color_map.append("steelblue")
        color_maps.append(color_map)
    return color_maps
