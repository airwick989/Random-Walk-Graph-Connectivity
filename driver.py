import networkx as nx
from visualize_graph_walk import GraphWalkVisualizer
import graph_functions as gf

#Initialize a directed networkx graph with many nodes and edges
G = nx.DiGraph()    #IMPORTANT TO CHANGE!!!
G.add_edges_from(gf.preMadeGraphs['many-nodes'])

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