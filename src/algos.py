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
        # add neighbors to stack
        for neighbor in graph.neighbors(cur_node):
            stack.append(neighbor)
        # add new color_map to color_maps
        color_map = []
        for node in graph.nodes:
            if node in visited:
                color_map.append("green")
            else:
                color_map.append("steel-blue")
        color_maps.append(color_map)
    return color_maps
