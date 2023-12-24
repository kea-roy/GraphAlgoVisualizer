import json
import tkinter
from tkinter import *
from tkinter import filedialog
import networkx as nx
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

matplotlib.use("TkAgg")


# Function that takes in name of algorithm and adjusts requirements
def on_algo_selection_change(algoName):
    print(algoName)


# Create Graph

graph = nx.DiGraph()
graph.add_nodes_from('ABCDEFGH')
graph.add_edges_from([
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

layout = {
    'A': [0, 1], 'B': [1, 2], 'C': [1, 1], 'D': [1, 0],
    'E': [2, 2], 'F': [2, 1], 'G': [2, 0], 'H': [3, 1],
}


# layout = nx.spring_layout(graph,seed=1)
def update_graph(graph):
    f = plt.Figure(figsize=(5, 5), dpi=100)
    a = f.add_subplot(111)
    # a.set_facecolor("w")
    labelMap = {}
    colorList = []

    for u, v, e in graph.edges(data=True):
        label = '{}/{}'.format(e['flow'], e['capacity'])
        color = 'green' if e['flow'] < e['capacity'] else 'red'
        labelMap[(u, v)] = label
        colorList.append(color)

    print(labelMap)
    print(colorList)

    nx.draw_networkx_edges(graph, layout, edge_color=colorList, ax=a, node_size=600)
    nx.draw_networkx_edge_labels(graph, layout, edge_labels=labelMap, label_pos=0.7, ax=a)
    nx.draw_networkx_nodes(graph, layout, node_color='steelblue', node_size=600, ax=a)
    nx.draw_networkx_labels(graph, layout, ax=a)

    # create matplotlib canvas using figure `f` and assign to widget `window`
    canvas = FigureCanvasTkAgg(f, window)

    # get canvas as tkinter's widget and `grid` in widget `window`
    canvas.get_tk_widget().grid(row=0, column=0, rowspan=1)


# Create Window
window = Tk()
window.title("Window")

# Create Frame
widget_frame = Frame(window)
widget_frame.grid(row=0, column=1, sticky=N)

# Create Widgets
# Label
Label(widget_frame, text="Control Panel").grid(row=0, column=0, sticky=EW)
# InputField
inputField = Entry(widget_frame, justify='center')
inputField.grid(row=1, column=0)


# Buttons

def select_file():
    filetypes = (
        ('text files', '*.txt'),
    )

    file = filedialog.askopenfile(
        title='Select Text File with Graph',
        initialdir='/',
        filetypes=filetypes)

    return file


def import_graph():
    file = select_file()
    if file is None:
        return
    new_graph = nx.read_edgelist(file, create_using=nx.DiGraph, nodetype=str)
    update_graph(new_graph)


openFileButton = Button(widget_frame, text="Import Graph from File", command=import_graph)
openFileButton.grid(row=6)


def add_edge():
    inp = inputField.get().strip()
    words = inp.split(" ")
    if len(words) == 2:
        graph.add_edge(words[0], words[1])
    elif len(words) > 2:
        new_str = inp.split(" ",2)[-1].replace("'", '"')
        print(new_str)
        graph.add_edge(words[0], words[1], **json.loads(new_str))
    update_graph(graph)


cmdButton = Button(widget_frame, text="Add Edge", command=add_edge)
cmdButton.grid(row=3, column=0, sticky=EW, padx=16)

button_frame = Frame(widget_frame)
button_frame.grid(row=5)


def backPressed():
    print("back")


backButton = Button(button_frame, text="<", command=backPressed)
backButton.grid(row=1, column=0, sticky=EW)


def nextPressed():
    print("next")


nextButton = Button(button_frame, text=">", command=nextPressed)
nextButton.grid(row=1, column=1, sticky=EW)

# Menu
selectedAlgo = tkinter.StringVar(window)
selectedAlgo.set("Select An Algorithm")
optionList = ["DFS", "BFS", "Dijkstra's", "Prim's", "Kruskal's", "Ford-Fulkerson"]
questionMenu = OptionMenu(widget_frame, selectedAlgo, *optionList, command=on_algo_selection_change)
questionMenu.grid(row=4, column=0, sticky=EW, padx=20)

# get selected option via selectedAlgo.get()

window.mainloop()

# Create an Undirected Graph
# UndirectedGraph = nx.Graph()


# edge_list = [(0, 1), (1, 2), (2, 3), (3, 5), (1, 4), (2, 4)]
# color_map = []
# G1 = nx.DiGraph()
# G1.add_edges_from(edge_list, )
#
# G2 = nx.complete_graph(5, create_using=nx.DiGraph)
# G2 = nx.relabel_nodes(G2, {0: "A", 1: "B", 2: "C", 3: "D", 4: "E"})
# G_connector = nx.from_edgelist([(0, "A"), ("A", 0)], create_using=nx.DiGraph)
#
# G = nx.compose_all([G1, G2, G_connector])
# for node in G:
#     if isinstance(node, str) and node < 'F':
#         color_map.append('red')
#     elif isinstance(node, int):
#         if node < 2:
#             color_map.append('red')
#         else:
#             color_map.append('blue')
#     else:
#         color_map.append('blue')
#
# print(color_map)
# nx.draw(G, node_color=color_map, with_labels=True)
# plt.show()

# Create a Directed Graph
# DirectedGraph = nx.DiGraph()
#
# DirectedGraph.add_edge(1, 2, weight=0.9)
# DirectedGraph.add_edge(2, 3, weight=1.0)
# DirectedGraph.add_edge(1, 2, weight=1.2)
# DirectedGraph.add_edge("A", "B", weight=1.3)
# DirectedGraph.add_node("C")
# DirectedGraph.add_node(print)
#
# edge_list = [(1, 2), (2, 3), (3, 5), (6, 7), (1, 4), (2, 4)]
#
# # G = nx.from_edgelist(edge_list, create_using=nx.DiGraph)
# nx.draw(G, with_labels=True)
#
# # To access degree of a node
# print(dict(G.degree)[2])
#
# # UndirectedGraph = nx.from_edgelist(edge_list)
#
# # UndirectedGraph = nx.Graph()
# # UndirectedGraph.add_edges_from(edge_list)
# #
# # adjMatrix = np.array([[0, 1, 1],
# #                       [0, 0, 0],
# #                       [0, 0, 0]])
# #
# # UndirectedGraph2 = nx.from_numpy_array(adjMatrix, create_using=nx.DiGraph)
#
# # nx.draw_spring(UndirectedGraph2, with_labels=True)
# plt.show()
