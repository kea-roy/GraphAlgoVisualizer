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


def get_dijkstras_color_maps(graph: nx.Graph, s_node: str) -> tuple[list[list[str]],list[list[str]]]:
    color_maps = []
    edge_color_maps = []
    dist = {}
    prev = {}
    entry_finder = {}
    visited = []
    used_edges = []
    heap = []
    entry = [0, s_node, None]
    entry_finder[s_node] = entry
    heappush(heap, entry)
    prev.update({s_node: None})
    while len(heap) > 0:
        cur_dist, cur_node, prev_node = heappop(heap)
        if cur_node == '<removed>':  # outdated value
            continue
        used_edges.append((prev_node, cur_node))
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
        # add new edge_color_map to edge_color_maps
        edge_color_map = []
        for u, v in graph.edges():
            if (u, v) in used_edges or (v, u) in used_edges:
                edge_color_map.append("green")
            else:
                edge_color_map.append("red")
        edge_color_maps.append(edge_color_map)
    return color_maps, edge_color_maps


def get_prims_color_maps(graph: nx.Graph) -> tuple[list[list[str]], list[list[str]]]:
    color_maps = []
    edge_color_maps = []
    mst_edges = []
    heap = []
    first_node = list(graph.nodes)[0]
    visited = {first_node}
    color_map = []
    for node in graph.nodes:
        if node in visited:
            color_map.append("green")
        else:
            color_map.append("steelblue")
    color_maps.append(color_map)
    # add new edge_color_map to edge_color_maps
    edge_color_map = []
    for u, v, d in graph.edges(data=True):
        if (u, v, d) in mst_edges or (v, u, d) in mst_edges:
            edge_color_map.append("green")
        else:
            edge_color_map.append("red")
    edge_color_maps.append(edge_color_map)
    # add all edges leaving first node to heap
    for v, d in graph.adj[first_node].items():
        weight = d.get('weight', 1.0)
        heappush(heap, (weight, first_node, v, d))
    while len(heap) > 0:
        weight, from_node, cur_node, d = heappop(heap)
        if cur_node in visited:
            continue
        mst_edges.append((from_node, cur_node, d))
        visited.add(cur_node)
        # add outgoing edges to queue
        for to_node, data in graph.adj[cur_node].items():
            if to_node in visited:
                continue
            weight = data.get('weight', 1.0)
            heappush(heap, (weight, cur_node, to_node, data))
        # add new color_map to color_maps
        color_map = []
        for node in graph.nodes:
            if node in visited:
                color_map.append("green")
            else:
                color_map.append("steelblue")
        color_maps.append(color_map)
        # add new edge_color_map to edge_color_maps
        edge_color_map = []
        for u, v, d in graph.edges(data=True):
            if (u, v, d) in mst_edges or (v, u, d) in mst_edges:
                edge_color_map.append("green")
            else:
                edge_color_map.append("red")
        edge_color_maps.append(edge_color_map)
    print(mst_edges)
    return color_maps, edge_color_maps


def get_kruskals_color_maps(graph: nx.Graph) -> tuple[list[list[str]], list[list[str]]]:
    color_maps = []
    edge_color_maps = []
    mst_edges = []
    heap = []
    for u,v,d in graph.edges(data=True):
        weight = d.get('weight',1.0)
        heappush(heap,(weight, u, v, d))
    visited = set()
    color_map = []
    for node in graph.nodes:
        if node in visited:
            color_map.append("green")
        else:
            color_map.append("steelblue")
    color_maps.append(color_map)
    # add new edge_color_map to edge_color_maps
    edge_color_map = []
    for u, v, d in graph.edges(data=True):
        if (u, v, d) in mst_edges or (v, u, d) in mst_edges:
            edge_color_map.append("green")
        else:
            edge_color_map.append("red")
    edge_color_maps.append(edge_color_map)
    while len(heap) > 0:
        weight, from_node, cur_node, d = heappop(heap)
        if from_node in visited and cur_node in visited:
            continue
        mst_edges.append((from_node, cur_node, d))
        visited.add(cur_node)
        visited.add(from_node)
        # add new color_map to color_maps
        color_map = []
        for node in graph.nodes:
            if node in visited:
                color_map.append("green")
            else:
                color_map.append("steelblue")
        color_maps.append(color_map)
        # add new edge_color_map to edge_color_maps
        edge_color_map = []
        for u, v, d in graph.edges(data=True):
            if (u, v, d) in mst_edges or (v, u, d) in mst_edges:
                edge_color_map.append("green")
            else:
                edge_color_map.append("red")
        edge_color_maps.append(edge_color_map)
    return color_maps, edge_color_maps
