import numpy as np 
import time 
from ezGraph import *

# Finite Difference Model

# PARAMETERS
dt = 1.
nsteps = 20

r = 2.25    # radius (cm)
Qin = 5     # Volume inflow rate: (cubic cm / s)
h = 0       # Initial height (cm)

# GRAPH
graph = ezGraph(xmax=30, ymin=0, ymax=10, xLabel="Time (s)", yLabel="Height (cm)")
graph.add(0, h)             # add initial values


# TIME LOOP
for t in range(1, nsteps):
    modelTime = t * dt

    dh = Qin * dt / (np.pi * r**2)    # find the change in height
    h = h + dh                      # update height
    
    print(modelTime, h)
    graph.add(modelTime, h)
    graph.wait(0.1)

# DRAW GRAPH
graph.keepOpen()
    
