import json
import sys
import tkinter
import algos
import math
from tkinter import *
from tkinter import filedialog
from tkinter.messagebox import showerror
import networkx as nx
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tktooltip import ToolTip

matplotlib.use("TkAgg")

# Create Graph
graph = nx.DiGraph()
color_maps = []
edge_color_maps = []
iteration_index = 0
layout = {}
labelMap = {}
colorList = []
label_maps = []


def back_pressed():
    print("back")
    global iteration_index
    if iteration_index - 1 < 0:
        print("reached start")
        return
    iteration_index = iteration_index - 1
    update_colors(color_maps, iteration_index, edge_color_maps)
    iteration_label_text.set("{}/{}".format(iteration_index, len(color_maps) - 1))


def next_pressed():
    print("next")
    global iteration_index
    if iteration_index + 1 >= len(color_maps):
        print("reached end")
        return
    iteration_index = iteration_index + 1
    update_colors(color_maps, iteration_index, edge_color_maps)
    iteration_label_text.set("{}/{}".format(iteration_index, len(color_maps) - 1))


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
        algo_name = selectedAlgo.get()
        if algo_name in ['Ford-Fulkerson', "Dijkstra's", "Prim's", "Kruskal's"]:
            print("ERROR: Edge doesn't contain required information for", algo_name,
                  file=sys.stderr)
            showerror(message="ERROR: Edge doesn't contain required information for " + algo_name)
            return
        graph.add_edge(words[0], words[1])
    elif len(words) > 2:
        new_str = inp.split(" ", 2)[-1].replace("'", '"')
        try:
            attributes = json.loads(new_str)
            data_tuple = ()
            algo_name = selectedAlgo.get()
            if algo_name == 'Ford-Fulkerson':
                data_tuple = (('capacity', int), ('flow', int),)
            elif algo_name in ["Dijkstra's", "Prim's", "Kruskal's"]:
                data_tuple = (('weight', float),)
            if check_edge(attributes, data_tuple):
                graph.add_edge(words[0], words[1], **attributes)
            else:
                print("ERROR: Edge doesn't contain required information for", algo_name,
                      file=sys.stderr)
                showerror(
                    message="ERROR: Edge doesn't contain required information for " + algo_name)
                return
        except json.decoder.JSONDecodeError as error:
            print("ERROR: Couldn't parse input as JSON", type(error).__name__, "–", error,
                  file=sys.stderr)
            showerror(message="ERROR: Couldn't parse input as JSON " + type(error).__name__ + " – "
                              + str(error))
            return
    update_graph(graph)


def check_edge(attributes, data_tuple) -> bool:
    if not isinstance(attributes, dict):
        return False
    for itemName, className in data_tuple:
        if itemName not in attributes:
            return False
    return True


def check_requirements(graph_to_check, data_tuple) -> bool:
    if len(graph_to_check.nodes) == 0:
        return False
    for u, v, e in graph_to_check.edges(data=True):
        for itemName, className in data_tuple:
            if itemName in e:
                print(type(e[itemName]), className, isinstance(e[itemName], className))
            if itemName not in e or not isinstance(e[itemName], className):
                print("Error:", itemName, "data is not provided for edge", u, "-", v,
                      file=sys.stderr)
                showerror(
                    message="ERROR: " + itemName + " data is not provided for edge " + u + " - " + v)
                return False
    return True


def clear_canvas():
    global graph, f, axes, canvas
    f = plt.Figure(figsize=(8, 6), dpi=100)
    axes = f.add_subplot(111)
    # if window['bg'] == 'systemWindowBackgroundColor':  # On macOS
    #     color_tuple = window.winfo_rgb('systemWindowBackgroundColor2')
    #     color_tuple = (color_tuple[0]/65536, color_tuple[1]/65536, color_tuple[2]/65536)
    #     f.set_facecolor(color_tuple)
    #     axes.set_facecolor(color_tuple)
    canvas = FigureCanvasTkAgg(f, window)
    canvas.get_tk_widget().grid(row=0, column=0, rowspan=1)


# Function that takes in name of algorithm and adjusts requirements
def on_algo_selection_change(algo_name):
    global graph, f, axes, canvas
    data_tuple = ()
    if algo_name in ["DFS", "BFS"]:
        # Need a Directed/Undirected Graph and Start Node
        print("Start Node")
        startNodeLabel.grid(row=0, column=0)
        startNodeField.grid(row=0, column=1)
        sinkNodeLabel.grid_remove()
        sinkNodeField.grid_remove()
    elif algo_name == "Dijkstra's":
        # Need a Directed/Undirected Graph with weights and Start Node
        print("Start Node")
        startNodeLabel.grid(row=0, column=0)
        startNodeField.grid(row=0, column=1)
        sinkNodeLabel.grid_remove()
        sinkNodeField.grid_remove()
        data_tuple = (('weight', float),)
    elif algo_name in ["Prim's", "Kruskal's"]:
        # Need an Undirected Graph
        print("None")
        startNodeLabel.grid_remove()
        startNodeField.grid_remove()
        sinkNodeLabel.grid_remove()
        sinkNodeField.grid_remove()
        data_tuple = (('weight', float),)
    elif algo_name == "Ford-Fulkerson":
        # Need a Directed Graph with Capacities and Flows and Start Node and End Node
        print("Source Node and Sink Node")
        startNodeLabel.grid(row=0, column=0)
        startNodeField.grid(row=0, column=1)
        sinkNodeLabel.grid(row=1, column=0)
        sinkNodeField.grid(row=1, column=1)
        data_tuple = (('capacity', int), ('flow', int))
    # check default graph type is set correctly
    if len(graph.nodes) == 0:
        if type(graph) != nx.Graph and algo_name in ["Prim's", "Kruskal's"]:
            graph = nx.Graph()
        elif type(graph) != nx.DiGraph and algo_name == "Ford-Fulkerson":
            graph = nx.DiGraph()
    # if graph already added, check graph contains weight information otherwise remove graph
    if len(graph.nodes) > 0 and not check_requirements(graph, data_tuple):
        print("Current Graph does not meet requirements for", algo_name +
              ", removing graph...")
        # remove graph
        graph = nx.DiGraph()
    update_graph(graph)
    iteration_label_text.set("")


# layout = nx.spring_layout(graph,seed=1)
def update_colors(new_color_maps, i, new_edge_color_maps=None):
    global canvas
    clear_canvas()
    if new_edge_color_maps is not None and len(new_edge_color_maps) == len(new_color_maps):
        nx.draw_networkx_edges(graph, layout, edge_color=new_edge_color_maps[i], node_size=600,
                               ax=axes)
    else:
        nx.draw_networkx_edges(graph, layout, edge_color=colorList, node_size=600, ax=axes)
    nx.draw_networkx_nodes(graph, layout, node_color=new_color_maps[i], node_size=600, ax=axes)
    nx.draw_networkx_labels(graph, layout, ax=axes)
    if selectedAlgo.get() == 'Ford-Fulkerson':
        nx.draw_networkx_edge_labels(graph, layout, edge_labels=label_maps[i], label_pos=0.7,
                                     ax=axes)
    else:
        nx.draw_networkx_edge_labels(graph, layout, edge_labels=labelMap, label_pos=0.7, ax=axes)
    canvas = FigureCanvasTkAgg(f, window)
    canvas.get_tk_widget().grid(row=0, column=0, rowspan=1)


def update_graph(new_graph):
    global f, axes, graph, canvas, layout, labelMap, colorList
    clear_canvas()
    labelMap = {}
    colorList = []
    algo_name = selectedAlgo.get()

    for u, v, e in new_graph.edges(data=True):
        label = ''
        color = 'green'
        if algo_name == 'Ford-Fulkerson':
            label = '{}/{}'.format(e['flow'], e['capacity'])
            if e['flow'] >= e['capacity']:
                color = 'red'
            elif e['flow'] > 0:
                color = 'darkorange'
            else:
                color = 'green'
        elif algo_name in ["Dijkstra's", "Prim's", "Kruskal's"]:
            label = '{}'.format(e['weight'])
            color = 'red'
        labelMap[(u, v)] = label
        colorList.append(color)

    print(labelMap)
    print(colorList)
    if algo_name == 'Ford-Fulkerson':
        layout = nx.drawing.nx_agraph.graphviz_layout(new_graph, prog='dot', args='-Grankdir=LR')
    else:
        try:
            layout = nx.layout.planar_layout(new_graph)
        except nx.exception.NetworkXException:
            layout = nx.layout.spring_layout(new_graph, seed=1,
                                             k=5 / math.sqrt(len(new_graph.nodes)))
    nx.draw_networkx_edges(new_graph, layout, edge_color=colorList, ax=axes, node_size=600)
    nx.draw_networkx_nodes(new_graph, layout, node_color='steelblue', node_size=600, ax=axes)
    nx.draw_networkx_labels(new_graph, layout, ax=axes)
    nx.draw_networkx_edge_labels(new_graph, layout, edge_labels=labelMap, label_pos=0.7, ax=axes)

    # create matplotlib canvas using figure `f` and assign to widget `window`
    canvas = FigureCanvasTkAgg(f, window)

    # get canvas as tkinter's widget and `grid` in widget `window`
    canvas.get_tk_widget().grid(row=0, column=0, rowspan=1)
    graph = new_graph


def import_graph():
    graph_type = None
    node_type = None
    edge_type = None
    data_tuple = True
    algo_name = selectedAlgo.get()
    if algo_name == "DFS" or algo_name == "BFS":
        print("Directed/Undirected")
        graph_type = nx.Graph
        data_tuple = ()
    elif algo_name == "Dijkstra's":
        print("Directed/Undirected Weighted")
        graph_type = nx.Graph
        data_tuple = (('weight', float),)
    elif algo_name in ["Prim's", "Kruskal's"]:
        print("Undirected Weighted")
        graph_type = nx.Graph
        data_tuple = (('weight', float),)
    elif algo_name == "Ford-Fulkerson":
        print("Directed Capacity Flow")
        graph_type = nx.DiGraph
        data_tuple = (('capacity', int), ('flow', int),)
    else:
        print("ERROR: Step 1 Not Completed", file=sys.stderr)
        showerror(message="ERROR: Step 1 Not Completed")
        return
    file = select_file()
    if file is None:
        print("No file was selected")
        return
    try:
        new_graph = nx.read_edgelist(file, create_using=graph_type, nodetype=node_type,
                                     edgetype=edge_type)
        # check required data is all present
        if not check_requirements(new_graph, data_tuple):
            return
        # check it is connected if prims/kruskals
        if algo_name in ["Prim's", "Kruskal's"] and not nx.is_connected(new_graph):
            print("ERROR: Graph isn't connected, so", algo_name, "is not suitable",
                  file=sys.stderr)
            showerror(message="ERROR: Graph isn't connected, so " + algo_name + " is not suitable")
            return
    except TypeError as error:
        print("ERROR: File contents are not in correct format:", type(error).__name__, "–", error,
              file=sys.stderr)
        showerror(message="ERROR: File contents are not in correct format: " + type(error).__name__
                          + "–" + str(error))
        return
    update_graph(new_graph)


def get_msg_format() -> str:
    algo_name = selectedAlgo.get()
    if algo_name in ["Dijkstra's", "Prim's", "Kruskal's"]:
        return "Format: [from_node] [to_node] '{'weight':1.0}'"
    elif algo_name == "Ford-Fulkerson":
        return "Format: [from_node] [to_node] '{'flow':1, 'capacity':1}'"
    else:
        return "Format: [from_node] [to_node]"


def run_algo():
    # check step 1
    algo_name = selectedAlgo.get()
    if algo_name not in optionList:
        print("ERROR: Step 1 Not Completed", file=sys.stderr)
        showerror(message="ERROR: Step 1 Not Completed")
        return
    # check step 2
    if len(graph.nodes) == 0:
        print("ERROR: No graph has been added", file=sys.stderr)
        showerror(message="ERROR: No graph has been added")
        return
    # check step 3
    if startNodeField.winfo_ismapped():
        s_node = startNodeField.get()
        if s_node not in graph.nodes:
            print("ERROR: Start/Source Node", "'" + s_node + "'", "is not in graph",
                  file=sys.stderr)
            showerror(message="ERROR: Start/Source Node '"+s_node+"' is not in graph")
            return
    if sinkNodeField.winfo_ismapped():
        e_node = sinkNodeField.get()
        if e_node not in graph.nodes:
            print("ERROR: Sink Node'", "'" + e_node + "'", "is not in graph", file=sys.stderr)
            showerror(message="ERROR: Sink Node '"+e_node+"' is not in graph")
            return
    # run algorithm
    global color_maps, edge_color_maps, label_maps
    global iteration_index
    if algo_name == "DFS":
        print("DFS")
        s_node = startNodeField.get()
        color_maps = algos.get_dfs_color_maps(graph, s_node)
        update_colors(color_maps, 0)
    elif algo_name == "BFS":
        print("BFS")
        s_node = startNodeField.get()
        color_maps = algos.get_bfs_color_maps(graph, s_node)
        update_colors(color_maps, 0)
    elif algo_name == "Dijkstra's":
        print("Dijkstra")
        s_node = startNodeField.get()
        color_maps, edge_color_maps = algos.get_dijkstras_color_maps(graph, s_node)
        update_colors(color_maps, 0, edge_color_maps)
    elif algo_name == "Prim's":
        print("Prim")
        color_maps, edge_color_maps = algos.get_prims_color_maps(graph)
        update_colors(color_maps, 0, edge_color_maps)
    elif algo_name == "Kruskal's":
        print("Kruskal")
        color_maps, edge_color_maps = algos.get_kruskals_color_maps(graph)
        update_colors(color_maps, 0, edge_color_maps)
    elif algo_name == "Ford-Fulkerson":
        print("Ford-Fulkerson")
        source_node = startNodeField.get()
        sink_node = sinkNodeField.get()
        color_maps, edge_color_maps, label_maps = (
            algos.get_ford_fulkerson_color_maps(graph, source_node, sink_node))
        update_colors(color_maps, 0, edge_color_maps)
    # update iteration label
    iteration_index = 0
    iteration_label_text.set("{}/{}".format(iteration_index, len(color_maps) - 1))
    print(iteration_label_text.get())


# Create Window
window = Tk()
window.title("Graph Algorithm Visualizer")

# Create Plot
clear_canvas()

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
ToolTip(edgeInputField, msg=get_msg_format, delay=1.0, **{"width": "2000"})
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
backButton = Button(button_frame, text="<", command=back_pressed)
backButton.grid(row=0, column=0, sticky=EW)
nextButton = Button(button_frame, text=">", command=next_pressed)
nextButton.grid(row=0, column=1, sticky=EW)
iteration_label_text = tkinter.StringVar()
iteration_label = Label(button_frame, textvariable=iteration_label_text)
iteration_label.grid(row=1, column=0, sticky=EW, columnspan=2)

update_graph(graph)
window.mainloop()
