import networkx as nx

"""
- Intitalized a set of pre-made graphs which can be used for running examples
- Includes varying examples like connected-directed, disconnected-undirected, etc.
"""
preMadeGraphs = {
    "con-undir": [(1, 2), (2, 3), (3, 4), (4, 1), (2, 4), (3, 1)],
    "discon-undir": [(1, 2), (3, 4), (5, 6), (7, 5), (8, 6), (6, 9), (1, 5)],
    "con-dir": [(1, 2), (2, 3), (3, 1), (3, 4), (4, 5), (5, 2)],
    "discon-dir": [(1, 2), (2, 3), (3, 1), (4, 5), (5, 6), (6, 4)],
    "weakcon-dir": [(1, 2), (2, 3), (3, 1), (2, 5), (4, 5), (5, 6)],
    "many-nodes": [(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7), (4, 8), (4, 9), (5, 10), (5, 11), (6, 12), (6, 13), (7, 14), (7, 15), (8, 16), (8, 17), (9, 18), (9, 19), (10, 20)],
}

"""
- Uses networkx's built-in methods to check the connectivity of a graph
- Takes a networkx graph object as a required parameter
- Checks whether the graph is directed or not
    - If directed, check the weak and strong connectivity, return a tuple
    - If not directed, simply check the connectivity
"""
def getConnectivity(graph):
    if nx.is_directed(graph):
        return (nx.is_weakly_connected(graph), nx.is_strongly_connected(graph))
    else:
        return nx.is_connected(graph)

"""
- Uses networkx's built-in methods to obtain the connected components of a graph
- Takes a networkx graph object as a required parameter
- Checks whether the graph is directed or not
    - If directed, obtain the weakly and strongly connected components, return a tuple containing lists of each
    - If not directed, simply obtain the connected components
"""
def getConnectedComponents(graph):
    if nx.is_directed(graph):
        return(list(nx.weakly_connected_components(graph)), list(nx.strongly_connected_components(graph)))
    else:
        return list(nx.connected_components(graph))

#Function that uses the other class functions to print all connectivity insights for a graph
#Takes a networkx graph as a parameter
def printConnectivityInsights(graph):

    #If the graph is directed ...
    if nx.is_directed(graph):
        weak_comps, strong_comps = getConnectedComponents(graph)    #Obtain the weakly and strongly connected components
        print(f"Weakly Connected Components: {weak_comps}\nStrongly Connected Components: {strong_comps}")  #Print results of connected components
        is_weak_con, is_strong_con = getConnectivity(graph) #Check the weak and strong connectivity of the graph
        print(f"Weak Connectivity: {is_weak_con}\nStrong Connectivity: {is_strong_con}")    #Print results of connectivity
    else:
        #If the graph is not directed ...
        print(f"Connected Components: {getConnectedComponents(graph)}") #Obtain and print the connected components of the graph
        print(f"Is graph connected: {getConnectivity(graph)}") #Check and print the connectivity of the graph