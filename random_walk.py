import random

#Class defining an object that will perform random walks
class RandomWalker:
    """
    The Walker takes 2 parameters
        - The graph being traversed (a networkx graph object)
        - The index of the start node (must be in the graph)
    The path traversed by the walker begins at the start node 
    """
    def __init__(self, graph, start_node):
        self.graph = graph
        self.current_node = start_node
        self.path = [start_node]

    #Function for performing a single step in the traversal
    #Function will move the walker to an available subsequent node in the current path
    def step(self):
        #Obtain a list of reachable neighbors relative to the current node
        neighbors = list(self.graph.neighbors(self.current_node))

        #If any neighbors exist, do the following
        if len(neighbors) > 0:
            next_node = random.choice(neighbors)    #Select a random neighbor node
            self.path.append(next_node) #Append the selected node to the current path
            self.current_node = next_node   #Set the current node as the selected node (perform the step)
        return self.path

    #Perform a number of steps (using the step function), as set by a passed parameter to the function
    def walk(self, num_steps):
        for _ in range(num_steps):
            self.step()
        return self.path


"""
- An extension of the RandomWalker class which performs a number of random walks
- In addition to the parameters required for a Walker, a MultipleRandomWalker also takes the number of walks as a parameter
"""
class MultipleRandomWalker(RandomWalker):
    def __init__(self, graph, start_node, num_walks):
        # Initialize multiple walkers for the number of walks set
        self.walkers = [RandomWalker(graph, start_node) for _ in range(num_walks)]

    def walk_multiple(self, num_steps):
        # Perform multiple random walks for the maximum specified number of steps
        paths = [walker.walk(num_steps) for walker in self.walkers]
        return paths