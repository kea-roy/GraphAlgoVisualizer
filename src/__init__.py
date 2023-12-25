import json
import sys
import tkinter
import algos
from tkinter import *
from tkinter import filedialog
import networkx as nx
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

matplotlib.use("TkAgg")

# Create Graph
graph = nx.DiGraph()
# graph.add_nodes_from('ABCDEFGH')
# graph.add_edges_from([
#     ('A', 'B', {'capacity': 4, 'flow': 0}),
#     ('A', 'C', {'capacity': 5, 'flow': 0}),
#     ('A', 'D', {'capacity': 7, 'flow': 0}),
#     ('B', 'E', {'capacity': 7, 'flow': 0}),
#     ('C', 'E', {'capacity': 6, 'flow': 0}),
#     ('C', 'F', {'capacity': 4, 'flow': 0}),
#     ('C', 'G', {'capacity': 1, 'flow': 0}),
#     ('D', 'F', {'capacity': 8, 'flow': 0}),
#     ('D', 'G', {'capacity': 1, 'flow': 0}),
#     ('E', 'H', {'capacity': 7, 'flow': 0}),
#     ('F', 'H', {'capacity': 6, 'flow': 0}),
#     ('G', 'H', {'capacity': 4, 'flow': 0}),
#
# ])

layout = {
    'A': [0, 1], 'B': [1, 2], 'C': [1, 1], 'D': [1, 0],
    'E': [2, 2], 'F': [2, 1], 'G': [2, 0], 'H': [3, 1],
}


def backPressed():
    print("back")


def nextPressed():
    print("next")


def select_file():
    filetypes = (
        ('text files', '*.txt'),
    )

    file = filedialog.askopenfile(
        title='Select Text File with Graph',
        initialdir='/',
        filetypes=filetypes)

    return file


def add_edge():
    inp = edgeInputField.get().strip()
    words = inp.split(" ")
    if len(words) == 2:
        graph.add_edge(words[0], words[1])
    elif len(words) > 2:
        new_str = inp.split(" ", 2)[-1].replace("'", '"')
        try:
            attributes = json.loads(new_str)
            graph.add_edge(words[0], words[1], **attributes)
        except json.decoder.JSONDecodeError as error:
            print("ERROR: Couldn't parse input as JSON", type(error).__name__, "–", error,
                  file=sys.stderr)
            return
    update_graph(graph)


# Function that takes in name of algorithm and adjusts requirements
def on_algo_selection_change(algoName: StringVar):
    if algoName in ["DFS", "BFS"]:
        # Need a Directed/Undirected Graph and Start Node
        print("Start Node")
        startNodeLabel.grid(row=0, column=0)
        startNodeField.grid(row=0, column=1)
        sinkNodeLabel.grid_remove()
        sinkNodeField.grid_remove()
    elif algoName == "Dijkstra's":
        # Need a Directed/Undirected Graph with weights and Start Node
        print("Start Node")
        startNodeLabel.grid(row=0, column=0)
        startNodeField.grid(row=0, column=1)
        sinkNodeLabel.grid_remove()
        sinkNodeField.grid_remove()
    elif algoName in ["Prim's", "Kruskal's"]:
        # Need an Undirected Graph
        print("None")
        startNodeLabel.grid_remove()
        startNodeField.grid_remove()
        sinkNodeLabel.grid_remove()
        sinkNodeField.grid_remove()
    elif algoName == "Ford-Fulkerson":
        # Need a Directed Graph with Capacities and Flows and Start Node and End Node
        print("Source Node and Sink Node")
        startNodeLabel.grid(row=0, column=0)
        startNodeField.grid(row=0, column=1)
        sinkNodeLabel.grid(row=1, column=0)
        sinkNodeField.grid(row=1, column=1)


# layout = nx.spring_layout(graph,seed=1)
def update_graph(new_graph):
    f = plt.Figure(figsize=(5, 5), dpi=100)
    a = f.add_subplot(111)
    # a.set_facecolor("w")
    labelMap = {}
    colorList = []

    for u, v, e in new_graph.edges(data=True):
        label = '{}/{}'.format(e['flow'], e['capacity'])
        color = 'green' if e['flow'] < e['capacity'] else 'red'
        labelMap[(u, v)] = label
        colorList.append(color)

    print(labelMap)
    print(colorList)

    nx.draw_networkx_edges(new_graph, layout, edge_color=colorList, ax=a, node_size=600)
    nx.draw_networkx_edge_labels(new_graph, layout, edge_labels=labelMap, label_pos=0.7, ax=a)
    nx.draw_networkx_nodes(new_graph, layout, node_color='steelblue', node_size=600, ax=a)
    nx.draw_networkx_labels(new_graph, layout, ax=a)

    # create matplotlib canvas using figure `f` and assign to widget `window`
    canvas = FigureCanvasTkAgg(f, window)

    # get canvas as tkinter's widget and `grid` in widget `window`
    canvas.get_tk_widget().grid(row=0, column=0, rowspan=1)
    global graph
    graph = new_graph


def import_graph():
    graph_type = None
    node_type = None
    edge_type = None
    data_tuple = True
    algoName = selectedAlgo.get()
    if algoName == "DFS" or algoName == "BFS":
        print("Directed/Undirected")
        graph_type = nx.Graph
        data_tuple = ()
    elif algoName == "Dijkstra's":
        print("Directed/Undirected Weighted")
        graph_type = nx.Graph
        data_tuple = (('weight', float),)
    elif algoName in ["Prim's", "Kruskal's"]:
        print("Undirected Weighted")
        graph_type = nx.Graph
        data_tuple = (('weight', float),)
    elif algoName == "Ford-Fulkerson":
        print("Directed Capacity Flow")
        graph_type = nx.DiGraph
        data_tuple = (('capacity', int), ('flow', int),)
    else:
        print("ERROR: Step 1 Not Completed", file=sys.stderr)
        return
    file = select_file()
    if file is None:
        print("No file was selected")
        return
    try:
        new_graph = nx.read_edgelist(file, create_using=graph_type, nodetype=node_type,
                                     edgetype=edge_type)
        # check required data is all present
        for u, v, e in new_graph.edges(data=True):
            for itemName, className in data_tuple:
                if itemName in e:
                    print(type(e[itemName]), className, isinstance(e[itemName], className))
                if itemName not in e or not isinstance(e[itemName], className):
                    print("Invalid File:", itemName, "data is not provided for edge", u, "-", v,
                          file=sys.stderr)
                    return
    except TypeError as error:
        print("ERROR: File contents are not in correct format: ", type(error).__name__, "–", error,
              file=sys.stderr)
        return
    update_graph(new_graph)


def run_algo():
    # check step 1
    algo_name = selectedAlgo.get()
    if algo_name not in optionList:
        print("ERROR: Step 1 Not Completed", file=sys.stderr)
        return
    # check step 2
    if len(graph.nodes) == 0:
        print("ERROR: Graph not added", file=sys.stderr)
        return
    # check step 3
    if startNodeField.winfo_ismapped():
        s_node = startNodeField.get()
        if s_node not in graph.nodes:
            print("ERROR: Start/Source Node", "'" + s_node + "'", "is not in graph",
                  file=sys.stderr)
            return
    if sinkNodeField.winfo_ismapped():
        e_node = sinkNodeField.get()
        if e_node not in graph.nodes:
            print("ERROR: Sink Nod'", "'" + e_node + "'", "is not in graph", file=sys.stderr)
            return
    # run algorithm
    if algo_name == "DFS":
        print("DFS")
        s_node = startNodeField.get()
        algos.get_dfs_color_maps(graph, s_node)
    elif algo_name == "BFS":
        print("BFS")
    elif algo_name == "Dijkstra's":
        print("Dijkstra")
    elif algo_name == "Prim's":
        print("Prim")
    elif algo_name == "Kruskal's":
        print("Kruskal")
    elif algo_name == "Ford-Fulkerson":
        print("Ford-Fulkerson")


# Create Window
window = Tk()
window.title("Window")

# Create Frame
widget_frame = Frame(window)
widget_frame.grid(row=0, column=1, sticky=N)
# Control Panel
Label(widget_frame, text="Control Panel").grid(row=0, column=0, sticky=EW, pady=10)
# Step 1 Label
Label(widget_frame, text="Step 1: Select Algorithm").grid(row=1, column=0, sticky=EW, pady=10)
# Menu
selectedAlgo = tkinter.StringVar(window)
selectedAlgo.set("Select An Algorithm")
optionList = ["DFS", "BFS", "Dijkstra's", "Prim's", "Kruskal's", "Ford-Fulkerson"]
questionMenu = OptionMenu(widget_frame, selectedAlgo, *optionList, command=on_algo_selection_change)
questionMenu.grid(row=2, column=0, sticky=EW, padx=20)
# get selected option via selectedAlgo.get()
# Step 2 Label
Label(widget_frame, text="Step 2: Import Graph").grid(row=3, column=0, sticky=EW, pady=10)
# Import Graph Button
Label(widget_frame, text="via File").grid(row=4, column=0, sticky=EW)
openFileButton = Button(widget_frame, text="Import Graph from File", command=import_graph)
openFileButton.grid(row=5, column=0)
# Edge Input
Label(widget_frame, text="via Edge").grid(row=6, column=0, sticky=EW)
edgeInputField = Entry(widget_frame, justify='center')
edgeInputField.grid(row=7, column=0)
cmdButton = Button(widget_frame, text="Add Edge", command=add_edge)
cmdButton.grid(row=8, column=0, sticky=EW, padx=16)
# Step 3 Label
Label(widget_frame, text="Step 3: Input Required Info").grid(row=9, column=0, sticky=EW, pady=10)
# Input Field(s)
algo_required_fields_frame = Frame(widget_frame)
algo_required_fields_frame.grid(row=10, column=0)
startNodeLabel = Label(algo_required_fields_frame, text="Start Node")
# startNodeLabel.grid(row=0, column=0)
startNodeField = Entry(algo_required_fields_frame, justify='left')
# startNodeField.grid(row=0, column=1)
sinkNodeLabel = Label(algo_required_fields_frame, text="Sink Node")
# sinkNodeLabel.grid(row=1, column=0)
sinkNodeField = Entry(algo_required_fields_frame, justify='left')
# sinkNodeField.grid(row=1, column=1)
# Step 4 Label
Label(widget_frame, text="Step 4: Run Algorithm").grid(row=11, column=0, sticky=EW, pady=10)
# Run Button
runAlgoButton = Button(widget_frame, text="Run", command=run_algo)
runAlgoButton.grid(row=12, column=0)
# Control Steps Buttons
button_frame = Frame(widget_frame)
button_frame.grid(row=13, column=0)
backButton = Button(button_frame, text="<", command=backPressed)
backButton.grid(row=0, column=0, sticky=EW)
nextButton = Button(button_frame, text=">", command=nextPressed)
nextButton.grid(row=0, column=1, sticky=EW)

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
