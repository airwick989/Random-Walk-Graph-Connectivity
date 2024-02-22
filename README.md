# Random-Walk-Graph-Connectivity

## How to Run

1. Ensure that the required dependencies are installed:<br>
```pip install networkx```<br>```pip install matplotlib```<br>
You may also require ```pip install PyQt5``` to display the graphed walks.
2. Run ```driver.py```

### Notes on driver.py:
- Line 6 can be changed from ```nx.Graph()``` for undirected graphs or ```nx.DiGraph()``` for directed graphs
- Line 7 changes the premade graph used (see ```preMadeGraphs``` dictionary in ```graph_functions.py```
- Lines 10-12 can be modified for the desired start_node, num_steps and num_walks accordingly
