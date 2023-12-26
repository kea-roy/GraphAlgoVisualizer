import networkx as nx
from collections import deque
from heapq import *


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


def get_dijkstras_color_maps(graph: nx.Graph, s_node: str) -> list[list[str]]:
    color_maps = []
    dist = {}
    prev = {}
    entry_finder = {}
    visited = []
    heap = []
    entry = [0, s_node, None]
    entry_finder[s_node] = entry
    heappush(heap, entry)
    prev.update({s_node: None})
    while len(heap) > 0:
        cur_dist, cur_node, prev_node = heappop(heap)
        if cur_node == '<removed>':  # outdated value
            continue
        visited.append(cur_node)
        dist.update({cur_node: cur_dist})
        # add neighbors to queue
        for neighbor in graph.neighbors(cur_node):
            neigh_dist = dist[cur_node] + graph[cur_node][neighbor]['weight']
            if neigh_dist < dist.get(neighbor, float('inf')):
                if neighbor in entry_finder:
                    entry = entry_finder.pop(neighbor)
                    entry[1] = '<removed>'
                entry = [neigh_dist, neighbor, cur_node]
                entry_finder[neighbor] = entry
                heappush(heap, entry)
                dist.update({neighbor: neigh_dist})
                prev.update({neighbor: cur_node})
        # add new color_map to color_maps
        color_map = []
        for node in graph.nodes:
            if node in visited:
                color_map.append("green")
            elif node in dist:
                color_map.append("lightgreen")
            else:
                color_map.append("steelblue")
        color_maps.append(color_map)
    print(dist)
    print(prev)
    return color_maps
