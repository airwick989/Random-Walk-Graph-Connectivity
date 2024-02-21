import networkx as nx
import matplotlib.pyplot as plt
from random_walk import RandomWalker, MultipleRandomWalker

#Class defining an object that is used to visualize graphs and random walks on graphs
class GraphWalkVisualizer:
    """
    - Visualizer object takes a networkx graph object as input
    - Graph node positioning used is the networkx spring layout
    - Default figure (visualization size) is 10x10 
    """
    def __init__(self, graph):
        self.graph = graph
        self.pos = nx.spring_layout(self.graph)
        self.figsize=(10,10)

    #Function which uses matplotlip and networkx draw methods to produce a visualization of a graph
    def drawGraph(self):
        fig = plt.figure(figsize=self.figsize)
        nx.draw_networkx_nodes(self.graph, self.pos, node_color='b')    #Draw nodes
        nx.draw_networkx_edges(self.graph, self.pos, edgelist=self.graph.edges, edge_color='b') #Draw edges
        nx.draw_networkx_labels(self.graph, self.pos, font_size=12, font_color="w") #Draw labels

    """
    - Function which uses matplotlip, networkx draw methods, and a RandomWalker object to produce a visualization of a random walk along a graph
    - Function takes a start node and max number of steps as required parameters
    - isMultiple, fig, and walk_count parameters are used by the drawMultiWalk function and do not ever need to be set by the user
    """
    def drawWalk(self, start_node, num_steps, isMultiple=False, fig=None, walk_count=0, path=[]):
        grid_size = int(len(path)**0.5) + 1  # Adjust grid size (for plotting subplots) based on the length of the path
        
        #If multiple walks are being visualized, draw subplots instead of a single figure
        if isMultiple:
            print(f"Random Walk {walk_count}: {path}")
            ax = fig.add_subplot(grid_size, grid_size, walk_count)  #initalize subplot
            ax.set_title(f"Random Walk {walk_count}")

            #For each subplot ...
            nx.draw_networkx_nodes(self.graph, self.pos, node_color='b', ax=ax) #Draw nodes
            nx.draw_networkx_edges(self.graph, self.pos, edgelist=self.graph.edges, edge_color='b', ax=ax) #Draw edges of graph
            nx.draw_networkx_labels(self.graph, self.pos, font_size=12, font_color="w", ax=ax) #Draw labels
            nx.draw_networkx_edges(self.graph.to_directed(), self.pos, edgelist=list(zip(path, path[1:])), edge_color='r', width=2, ax=ax) #Draw directed edges for the path walked
        else:
            #If only one walk is being visualized ...
            walker = RandomWalker(self.graph, start_node)   #Initialize a walker object
            path = walker.walk(num_steps)   #Obtain the path traversed by the walker
            print(f"Random Walk Path: {path}")
            self.drawGraph()    #Draw the graph using the class function
            nx.draw_networkx_edges(self.graph.to_directed(), self.pos, edgelist=list(zip(path, path[1:])), edge_color='r', width=2) #Draw directed edges for the path walked

    """
    - Function which uses matplotlip, networkx draw methods, a MultipleRandomWalker object, and the drawWalk class function to produce a visualization of multiple random walks along a graph
    - Like drawWalk, takes start node and max number of steps as parameters, but also takes the number of walks
    """
    def drawMultiWalk(self, start_node, num_walks, num_steps_per_walk):
        multi_walker = MultipleRandomWalker(self.graph, start_node, num_walks)  #Initialize a multiple walker object
        paths = multi_walker.walk_multiple(num_steps_per_walk)  #Obtain all paths from all walks

        fig = plt.figure(figsize=self.figsize)  #Initialize a figure to draw subplots on
        
        #For the number of paths there are, draw the walk in a subplot using the drawWalk class function
        for i, path in enumerate(paths):
            self.drawWalk(start_node, num_steps_per_walk, True, fig, i + 1, path)

    #Function which displays all the visualizations which have been drawen
    def visualize(self):
        plt.tight_layout()
        plt.show()