import numpy as np
import time
from ezGraph import *

#GRAPH THE FUNCTION f(x) = x**0.5

# SET UP GRAPH
graph = ezGraph()

for x in range(10):
    y = x**0.5
    graph.add(x, y)     # Add points to plot
    graph.wait(0.5)     # Pause for half a second
    

# DRAW GRAPH
graph.keepOpen()    # keep graph open when done
