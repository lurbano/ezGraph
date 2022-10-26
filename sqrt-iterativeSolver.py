import numpy as np
import time
from ezGraph import *

# INPUT
target = 25     # value to find the square root of

# INITIALIZATON SETTINGS
g = 1         # initial guess

conv = 0.001    # convergence criteria (run progra until we're this
                #  close to the target)

# INITIAL TEST
test = g * g    # square the guess to see if it is the same as the target
diff = abs(test-target) # the difference between the target and the test
i = 0           # itteraton 

# SET UP FOR OUTPUT FOR EACH ITERATION
graph = ezGraph()
graph.add(i, g)
graph.wait(1)                # pause for 2 seconds

while (diff > conv):    # run while the difference is greater than our convergence criteria 
    i += 1
    g = (g + target/g)/2
    test = g * g
    diff = abs(test-target) # check how close to the target we are

    # gather output data for this iteration
    graph.add(i, g)
    graph.wait(1)
    

# DRAW GRAPH
graph.keepOpen()    # keep graph open
