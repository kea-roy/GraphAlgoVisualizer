import unittest

import networkx as nx
import src.algos as algos


class TestAlgorithmMethods(unittest.TestCase):
    # Several Test Graphs
    # single node test graph
    single_node_graph = nx.Graph()
    single_node_graph.add_nodes_from('A')
    # two node test graph
    two_node_graph = nx.Graph()
    two_node_graph.add_nodes_from('AB')
    two_node_graph.add_edges_from([
        ('A', 'B', {'capacity': 4, 'flow': 0, 'weight': 1.0}),
    ])
    # three node test graph
    three_node_graph = nx.Graph()
    three_node_graph.add_nodes_from('ABC')
    three_node_graph.add_edges_from([
        ('A', 'B', {'capacity': 1, 'flow': 0, 'weight': 1.0}),
        ('A', 'C', {'capacity': 2, 'flow': 0, 'weight': 1.0}),
        ('B', 'C', {'capacity': 3, 'flow': 0, 'weight': 1.0}),
    ])
    # five node test graph
    five_node_graph = nx.Graph()
    five_node_graph.add_nodes_from('ABCDE')
    five_node_graph.add_edges_from([
        ('A', 'B', {'capacity': 1, 'flow': 0, 'weight': 1.0}),
        ('A', 'C', {'capacity': 1, 'flow': 0, 'weight': 1.0}),
        ('B', 'D', {'capacity': 1, 'flow': 0, 'weight': 1.0}),
        ('B', 'E', {'capacity': 1, 'flow': 0, 'weight': 1.0}),
        ('C', 'D', {'capacity': 1, 'flow': 0, 'weight': 1.0}),
        ('C', 'E', {'capacity': 1, 'flow': 0, 'weight': 1.0}),
        ('D', 'E', {'capacity': 1, 'flow': 0, 'weight': 1.0}),
    ])
    # dijkstra, prims, and kruskals test graph
    dijkstra_weight_test_graph = nx.Graph()
    dijkstra_weight_test_graph.add_nodes_from('ABC')
    dijkstra_weight_test_graph.add_edges_from([
        ('A', 'B', {'capacity': 1, 'flow': 0, 'weight': 1.0}),
        ('A', 'C', {'capacity': 2, 'flow': 0, 'weight': 10.0}),
        ('B', 'C', {'capacity': 3, 'flow': 0, 'weight': 1.0}),
    ])
    # ford-fulkerson test graph
    ford_fulkerson_test_graph = nx.DiGraph()
    ford_fulkerson_test_graph.add_nodes_from('ABCDEFGH')
    ford_fulkerson_test_graph.add_edges_from([
        ('A', 'B', {'capacity': 4, 'flow': 0}),
        ('A', 'C', {'capacity': 5, 'flow': 0}),
        ('A', 'D', {'capacity': 7, 'flow': 0}),
        ('B', 'E', {'capacity': 7, 'flow': 0}),
        ('C', 'E', {'capacity': 6, 'flow': 0}),
        ('C', 'F', {'capacity': 4, 'flow': 0}),
        ('C', 'G', {'capacity': 1, 'flow': 0}),
        ('D', 'F', {'capacity': 8, 'flow': 0}),
        ('D', 'G', {'capacity': 1, 'flow': 0}),
        ('E', 'H', {'capacity': 7, 'flow': 0}),
        ('F', 'H', {'capacity': 6, 'flow': 0}),
        ('G', 'H', {'capacity': 4, 'flow': 0}),
    ])

    # run those test graphs

    def test_dfs_color_maps(self):
        # single node dfs graph should finish in one iteration and return the node colored green
        self.assertEqual(algos.get_dfs_color_maps(self.single_node_graph, 'A'), [['green']])
        # two node dfs graph should finish in two iterations
        self.assertEqual(algos.get_dfs_color_maps(self.two_node_graph, 'A'),
                         [['green', 'steelblue'], ['green', 'green']])
        # three node dfs graph should finish in three iterations and choose the smallest
        # lexicographical labelled node when there are multiple options
        self.assertEqual(algos.get_dfs_color_maps(self.three_node_graph, 'A'),
                         [['green', 'steelblue', 'steelblue'], ['green', 'green', 'steelblue'],
                          ['green', 'green', 'green']])
        # five node dfs graph should finish in five iterations and explore nodes depth first
        self.assertEqual(algos.get_dfs_color_maps(self.five_node_graph, 'A'),
                         [['green', 'steelblue', 'steelblue', 'steelblue', 'steelblue'],
                          ['green', 'green', 'steelblue', 'steelblue', 'steelblue'],
                          ['green', 'green', 'steelblue', 'green', 'steelblue'],
                          ['green', 'green', 'green', 'green', 'steelblue'],
                          ['green', 'green', 'green', 'green', 'green']])

    def test_bfs_color_maps(self):
        # single node bfs graph should finish in one iteration and return the node colored green
        self.assertEqual(algos.get_bfs_color_maps(self.single_node_graph, 'A'), [['green']])
        # two node bfs graph should finish in two iterations
        self.assertEqual(algos.get_bfs_color_maps(self.two_node_graph, 'A'),
                         [['green', 'steelblue'], ['green', 'green']])
        # three node bfs graph should finish in three iterations and choose the smallest
        # lexicographical labelled node when there are multiple options
        self.assertEqual(algos.get_bfs_color_maps(self.three_node_graph, 'A'),
                         [['green', 'steelblue', 'steelblue'], ['green', 'green', 'steelblue'],
                          ['green', 'green', 'green']])
        # five node bfs graph should finish in five iterations and explore nodes breadth first
        self.assertEqual(algos.get_bfs_color_maps(self.five_node_graph, 'A'),
                         [['green', 'steelblue', 'steelblue', 'steelblue', 'steelblue'],
                          ['green', 'green', 'steelblue', 'steelblue', 'steelblue'],
                          ['green', 'green', 'green', 'steelblue', 'steelblue'],
                          ['green', 'green', 'green', 'green', 'steelblue'],
                          ['green', 'green', 'green', 'green', 'green']])

    def test_dijkstras_color_maps(self):
        # single node graph should finish in one iteration and return the node colored green
        self.assertEqual(algos.get_dijkstras_color_maps(self.single_node_graph, 'A'),
                         ([['green']], [[]]))
        # two node graph should finish in two iterations
        self.assertEqual(algos.get_dijkstras_color_maps(self.two_node_graph, 'A'),
                         ([['green', 'lightgreen'], ['green', 'green']], [['red'], ['green']]))
        # three node graph should finish in three iterations and choose the smallest
        # lexicographical labelled node when there are ties in weight
        self.assertEqual(algos.get_dijkstras_color_maps(self.three_node_graph, 'A'),
                         ([['green', 'lightgreen', 'lightgreen'], ['green', 'green', 'lightgreen'],
                           ['green', 'green', 'green']],
                          [['red', 'red', 'red'], ['green', 'red', 'red'],
                           ['green', 'green', 'red']]))
        # five node graph should finish in five iterations and choose the smallest
        # lexicographical labelled node when there are ties in weight
        self.assertEqual(algos.get_dijkstras_color_maps(self.five_node_graph, 'A'),
                         ([['green', 'lightgreen', 'lightgreen', 'steelblue', 'steelblue'],
                           ['green', 'green', 'lightgreen', 'lightgreen', 'lightgreen'],
                           ['green', 'green', 'green', 'lightgreen', 'lightgreen'],
                           ['green', 'green', 'green', 'green', 'lightgreen'],
                           ['green', 'green', 'green', 'green', 'green']],
                          [['red', 'red', 'red', 'red', 'red', 'red', 'red'],
                           ['green', 'red', 'red', 'red', 'red', 'red', 'red'],
                           ['green', 'green', 'red', 'red', 'red', 'red', 'red'],
                           ['green', 'green', 'green', 'red', 'red', 'red', 'red'],
                           ['green', 'green', 'green', 'green', 'red', 'red', 'red']]))
        # dijkstra should explore smallest weight first
        self.assertEqual(algos.get_dijkstras_color_maps(self.dijkstra_weight_test_graph, 'A'),
                         ([['green', 'lightgreen', 'lightgreen'], ['green', 'green', 'lightgreen'],
                           ['green', 'green', 'green']],
                          [['red', 'red', 'red'], ['green', 'red', 'red'],
                           ['green', 'red', 'green']]))

    def test_prims_color_maps(self):
        # single node graph should finish in one iteration and return the node colored green
        self.assertEqual(algos.get_prims_color_maps(self.single_node_graph),
                         ([['green']], [[]]))
        # two node graph should finish in two iterations
        self.assertEqual(algos.get_prims_color_maps(self.two_node_graph),
                         ([['green', 'steelblue'], ['green', 'green']], [['red'], ['green']]))
        # three node graph should finish in three iterations and choose the smallest
        # lexicographical labelled node when there are ties in weight
        self.assertEqual(algos.get_prims_color_maps(self.three_node_graph),
                         ([['green', 'steelblue', 'steelblue'], ['green', 'green', 'steelblue'],
                           ['green', 'green', 'green']],
                          [['red', 'red', 'red'], ['green', 'red', 'red'],
                           ['green', 'green', 'red']]))
        # five node graph should finish in five iterations and choose the smallest
        # lexicographical labelled node when there are ties in weight
        self.assertEqual(algos.get_prims_color_maps(self.five_node_graph),
                         ([['green', 'steelblue', 'steelblue', 'steelblue', 'steelblue'],
                           ['green', 'green', 'steelblue', 'steelblue', 'steelblue'],
                           ['green', 'green', 'green', 'steelblue', 'steelblue'],
                           ['green', 'green', 'green', 'green', 'steelblue'],
                           ['green', 'green', 'green', 'green', 'green']],
                          [['red', 'red', 'red', 'red', 'red', 'red', 'red'],
                           ['green', 'red', 'red', 'red', 'red', 'red', 'red'],
                           ['green', 'green', 'red', 'red', 'red', 'red', 'red'],
                           ['green', 'green', 'green', 'red', 'red', 'red', 'red'],
                           ['green', 'green', 'green', 'green', 'red', 'red', 'red']]))
        # prim should explore based on edges leaving smallest node first
        self.assertEqual(algos.get_prims_color_maps(self.dijkstra_weight_test_graph),
                         ([['green', 'steelblue', 'steelblue'], ['green', 'green', 'steelblue'],
                           ['green', 'green', 'green']],
                          [['red', 'red', 'red'], ['green', 'red', 'red'],
                           ['green', 'red', 'green']]))

    def test_kruskals_color_maps(self):
        # single node graph should finish in one iteration and return the node colored steelblue
        self.assertEqual(algos.get_kruskals_color_maps(self.single_node_graph),
                         ([['steelblue']], [[]]))
        # two node graph should finish in two iterations
        self.assertEqual(algos.get_kruskals_color_maps(self.two_node_graph),
                         ([['steelblue', 'steelblue'], ['green', 'green']], [['red'], ['green']]))
        # three node graph should finish in three iterations and choose the first added edge
        # when there are ties
        self.assertEqual(algos.get_kruskals_color_maps(self.three_node_graph),
                         ([['steelblue', 'steelblue', 'steelblue'], ['green', 'green', 'steelblue'],
                           ['green', 'green', 'green']],
                          [['red', 'red', 'red'], ['green', 'red', 'red'],
                           ['green', 'green', 'red']]))
        # five node graph should finish in five iterations and choose the first added edge
        # when there are ties
        self.assertEqual(algos.get_kruskals_color_maps(self.five_node_graph),
                         ([['steelblue', 'steelblue', 'steelblue', 'steelblue', 'steelblue'],
                           ['green', 'green', 'steelblue', 'steelblue', 'steelblue'],
                           ['green', 'green', 'green', 'steelblue', 'steelblue'],
                           ['green', 'green', 'green', 'green', 'steelblue'],
                           ['green', 'green', 'green', 'green', 'green']],
                          [['red', 'red', 'red', 'red', 'red', 'red', 'red'],
                           ['green', 'red', 'red', 'red', 'red', 'red', 'red'],
                           ['green', 'green', 'red', 'red', 'red', 'red', 'red'],
                           ['green', 'green', 'green', 'red', 'red', 'red', 'red'],
                           ['green', 'green', 'green', 'green', 'red', 'red', 'red']]))
        # kruskals should explore based on smallest edge first
        self.assertEqual(algos.get_kruskals_color_maps(self.dijkstra_weight_test_graph),
                         ([['steelblue', 'steelblue', 'steelblue'], ['green', 'green', 'steelblue'],
                           ['green', 'green', 'green']],
                          [['red', 'red', 'red'], ['green', 'red', 'red'],
                           ['green', 'red', 'green']]))

    def test_ford_fulkerson_color_maps(self):
        # should update flow graph correctly, always picking the routes in the residual
        # graph with the smallest lexicographical labelled node when there are multiple options
        self.assertEqual(
            algos.get_ford_fulkerson_color_maps(self.ford_fulkerson_test_graph, 'A', 'H'),
            ([['steelblue', 'steelblue', 'steelblue', 'steelblue', 'steelblue', 'steelblue',
               'steelblue', 'steelblue'],
              ['steelblue', 'steelblue', 'steelblue', 'steelblue', 'steelblue', 'steelblue',
               'steelblue', 'steelblue'],
              ['steelblue', 'steelblue', 'steelblue', 'steelblue', 'steelblue', 'steelblue',
               'steelblue', 'steelblue'],
              ['steelblue', 'steelblue', 'steelblue', 'steelblue', 'steelblue', 'steelblue',
               'steelblue', 'steelblue'],
              ['steelblue', 'steelblue', 'steelblue', 'steelblue', 'steelblue', 'steelblue',
               'steelblue', 'steelblue'],
              ['steelblue', 'steelblue', 'steelblue', 'steelblue', 'steelblue', 'steelblue',
               'steelblue', 'steelblue'],
              ['steelblue', 'steelblue', 'steelblue', 'steelblue', 'steelblue', 'steelblue',
               'steelblue', 'steelblue']], [
                 ['green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green',
                  'green', 'green', 'green'],
                 ['green', 'green', 'darkorange', 'green', 'green', 'green', 'green', 'green',
                  'red', 'green', 'green', 'darkorange'],
                 ['green', 'green', 'red', 'green', 'green', 'green', 'green', 'darkorange', 'red',
                  'green', 'red', 'darkorange'],
                 ['green', 'darkorange', 'red', 'green', 'green', 'green', 'red', 'darkorange',
                  'red', 'green', 'red', 'darkorange'],
                 ['green', 'red', 'red', 'green', 'darkorange', 'green', 'red', 'darkorange', 'red',
                  'darkorange', 'red', 'darkorange'],
                 ['darkorange', 'red', 'red', 'darkorange', 'darkorange', 'green', 'red',
                  'darkorange', 'red', 'red', 'red', 'darkorange'],
                 ['darkorange', 'red', 'red', 'darkorange', 'darkorange', 'green', 'red',
                  'darkorange', 'red', 'red', 'red', 'darkorange']], [
                 {('A', 'B'): '0/4', ('A', 'C'): '0/5', ('A', 'D'): '0/7', ('B', 'E'): '0/7',
                  ('C', 'E'): '0/6', ('C', 'F'): '0/4', ('C', 'G'): '0/1', ('D', 'F'): '0/8',
                  ('D', 'G'): '0/1', ('E', 'H'): '0/7', ('F', 'H'): '0/6', ('G', 'H'): '0/4'},
                 {('A', 'B'): '0/4', ('A', 'C'): '0/5', ('A', 'D'): '1/7', ('B', 'E'): '0/7',
                  ('C', 'E'): '0/6', ('C', 'F'): '0/4', ('C', 'G'): '0/1', ('D', 'F'): '0/8',
                  ('D', 'G'): '1/1', ('E', 'H'): '0/7', ('F', 'H'): '0/6', ('G', 'H'): '1/4'},
                 {('A', 'B'): '0/4', ('A', 'C'): '0/5', ('A', 'D'): '7/7', ('B', 'E'): '0/7',
                  ('C', 'E'): '0/6', ('C', 'F'): '0/4', ('C', 'G'): '0/1', ('D', 'F'): '6/8',
                  ('D', 'G'): '1/1', ('E', 'H'): '0/7', ('F', 'H'): '6/6', ('G', 'H'): '1/4'},
                 {('A', 'B'): '0/4', ('A', 'C'): '1/5', ('A', 'D'): '7/7', ('B', 'E'): '0/7',
                  ('C', 'E'): '0/6', ('C', 'F'): '0/4', ('C', 'G'): '1/1', ('D', 'F'): '6/8',
                  ('D', 'G'): '1/1', ('E', 'H'): '0/7', ('F', 'H'): '6/6', ('G', 'H'): '2/4'},
                 {('A', 'B'): '0/4', ('A', 'C'): '5/5', ('A', 'D'): '7/7', ('B', 'E'): '0/7',
                  ('C', 'E'): '4/6', ('C', 'F'): '0/4', ('C', 'G'): '1/1', ('D', 'F'): '6/8',
                  ('D', 'G'): '1/1', ('E', 'H'): '4/7', ('F', 'H'): '6/6', ('G', 'H'): '2/4'},
                 {('A', 'B'): '3/4', ('A', 'C'): '5/5', ('A', 'D'): '7/7', ('B', 'E'): '3/7',
                  ('C', 'E'): '4/6', ('C', 'F'): '0/4', ('C', 'G'): '1/1', ('D', 'F'): '6/8',
                  ('D', 'G'): '1/1', ('E', 'H'): '7/7', ('F', 'H'): '6/6', ('G', 'H'): '2/4'},
                 {('A', 'B'): '3/4', ('A', 'C'): '5/5', ('A', 'D'): '7/7', ('B', 'E'): '3/7',
                  ('C', 'E'): '4/6', ('C', 'F'): '0/4', ('C', 'G'): '1/1', ('D', 'F'): '6/8',
                  ('D', 'G'): '1/1', ('E', 'H'): '7/7', ('F', 'H'): '6/6', ('G', 'H'): '2/4'}]))
        # Will stop at two iterations when the flow cannot be increased (ex: when there are no arcs)
        self.assertEqual(
            algos.get_ford_fulkerson_color_maps(self.ford_fulkerson_test_graph, 'H', 'A'),
            ([['steelblue', 'steelblue', 'steelblue', 'steelblue', 'steelblue', 'steelblue',
               'steelblue', 'steelblue'],
              ['steelblue', 'steelblue', 'steelblue', 'steelblue', 'steelblue', 'steelblue',
               'steelblue', 'steelblue'],
              ['steelblue', 'steelblue', 'steelblue', 'steelblue', 'steelblue', 'steelblue',
               'steelblue', 'steelblue'],
              ['steelblue', 'steelblue', 'steelblue', 'steelblue', 'steelblue', 'steelblue',
               'steelblue', 'steelblue'],
              ['steelblue', 'steelblue', 'steelblue', 'steelblue', 'steelblue', 'steelblue',
               'steelblue', 'steelblue'],
              ['steelblue', 'steelblue', 'steelblue', 'steelblue', 'steelblue', 'steelblue',
               'steelblue', 'steelblue'],
              ['steelblue', 'steelblue', 'steelblue', 'steelblue', 'steelblue', 'steelblue',
               'steelblue', 'steelblue'],
              ['steelblue', 'steelblue', 'steelblue', 'steelblue', 'steelblue', 'steelblue',
               'steelblue', 'steelblue']], [
                 ['darkorange', 'red', 'red', 'darkorange', 'darkorange', 'green', 'red',
                  'darkorange', 'red', 'red', 'red', 'darkorange'],
                 ['darkorange', 'red', 'darkorange', 'darkorange', 'darkorange', 'green', 'red',
                  'darkorange', 'green', 'red', 'red', 'darkorange'],
                 ['darkorange', 'red', 'darkorange', 'darkorange', 'darkorange', 'darkorange',
                  'green', 'darkorange', 'green', 'red', 'red', 'green'],
                 ['darkorange', 'red', 'green', 'darkorange', 'darkorange', 'darkorange', 'green',
                  'green', 'green', 'red', 'darkorange', 'green'],
                 ['darkorange', 'red', 'green', 'darkorange', 'darkorange', 'green', 'green',
                  'green', 'green', 'red', 'green', 'green'],
                 ['darkorange', 'green', 'green', 'darkorange', 'green', 'green', 'green', 'green',
                  'green', 'darkorange', 'green', 'green'],
                 ['green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green',
                  'green', 'green', 'green'],
                 ['green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green',
                  'green', 'green', 'green']], [
                 {('A', 'B'): '3/4', ('A', 'C'): '5/5', ('A', 'D'): '7/7', ('B', 'E'): '3/7',
                  ('C', 'E'): '4/6', ('C', 'F'): '0/4', ('C', 'G'): '1/1', ('D', 'F'): '6/8',
                  ('D', 'G'): '1/1', ('E', 'H'): '7/7', ('F', 'H'): '6/6', ('G', 'H'): '2/4'},
                 {('A', 'B'): '3/4', ('A', 'C'): '5/5', ('A', 'D'): '6/7', ('B', 'E'): '3/7',
                  ('C', 'E'): '4/6', ('C', 'F'): '0/4', ('C', 'G'): '1/1', ('D', 'F'): '6/8',
                  ('D', 'G'): '0/1', ('E', 'H'): '7/7', ('F', 'H'): '6/6', ('G', 'H'): '1/4'},
                 {('A', 'B'): '3/4', ('A', 'C'): '5/5', ('A', 'D'): '5/7', ('B', 'E'): '3/7',
                  ('C', 'E'): '4/6', ('C', 'F'): '1/4', ('C', 'G'): '0/1', ('D', 'F'): '5/8',
                  ('D', 'G'): '0/1', ('E', 'H'): '7/7', ('F', 'H'): '6/6', ('G', 'H'): '0/4'},
                 {('A', 'B'): '3/4', ('A', 'C'): '5/5', ('A', 'D'): '0/7', ('B', 'E'): '3/7',
                  ('C', 'E'): '4/6', ('C', 'F'): '1/4', ('C', 'G'): '0/1', ('D', 'F'): '0/8',
                  ('D', 'G'): '0/1', ('E', 'H'): '7/7', ('F', 'H'): '1/6', ('G', 'H'): '0/4'},
                 {('A', 'B'): '2/4', ('A', 'C'): '5/5', ('A', 'D'): '0/7', ('B', 'E'): '2/7',
                  ('C', 'E'): '5/6', ('C', 'F'): '0/4', ('C', 'G'): '0/1', ('D', 'F'): '0/8',
                  ('D', 'G'): '0/1', ('E', 'H'): '7/7', ('F', 'H'): '0/6', ('G', 'H'): '0/4'},
                 {('A', 'B'): '2/4', ('A', 'C'): '0/5', ('A', 'D'): '0/7', ('B', 'E'): '2/7',
                  ('C', 'E'): '0/6', ('C', 'F'): '0/4', ('C', 'G'): '0/1', ('D', 'F'): '0/8',
                  ('D', 'G'): '0/1', ('E', 'H'): '2/7', ('F', 'H'): '0/6', ('G', 'H'): '0/4'},
                 {('A', 'B'): '0/4', ('A', 'C'): '0/5', ('A', 'D'): '0/7', ('B', 'E'): '0/7',
                  ('C', 'E'): '0/6', ('C', 'F'): '0/4', ('C', 'G'): '0/1', ('D', 'F'): '0/8',
                  ('D', 'G'): '0/1', ('E', 'H'): '0/7', ('F', 'H'): '0/6', ('G', 'H'): '0/4'},
                 {('A', 'B'): '0/4', ('A', 'C'): '0/5', ('A', 'D'): '0/7', ('B', 'E'): '0/7',
                  ('C', 'E'): '0/6', ('C', 'F'): '0/4', ('C', 'G'): '0/1', ('D', 'F'): '0/8',
                  ('D', 'G'): '0/1', ('E', 'H'): '0/7', ('F', 'H'): '0/6', ('G', 'H'): '0/4'}]))


if __name__ == '__main__':
    unittest.main()
