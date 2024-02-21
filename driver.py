import networkx as nx
from visualize_graph_walk import GraphWalkVisualizer
import graph_functions as gf

#Initialize a directed networkx graph with many nodes and edges
G = nx.DiGraph()
G.add_edges_from([(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7), (4, 8), (4, 9), (5, 10), (5, 11), (6, 12), (6, 13), (7, 14), (7, 15), (8, 16), (8, 17), (9, 18), (9, 19), (10, 20)])

#Set the start node, max number of steps, and number of walks
start_node = 1
num_steps = 7
num_walks = 5

visualizer = GraphWalkVisualizer(G) #Initialize a visualizer object and pass the created graph to it
visualizer.drawGraph()  #Use the visualizer object to draw the graph
visualizer.drawWalk(start_node, num_steps)  #Perform a single walk and draw it using the predefined parameters
visualizer.drawMultiWalk(start_node, num_walks, num_steps)  #Perform multiple walks and draw them using the predefined parameters
gf.printConnectivityInsights(G) #Print the connectivity insights for the given graph

visualizer.visualize()  #Visualize (display) all drawn plots