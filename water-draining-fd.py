import numpy as np 
import time 
from ezGraph import *

# Finite Difference Model

# PARAMETERS
dt = 1
nsteps = 100

r = 2.25    # radius (cm)
Q = 0       # Volume inflow rate (dV/dt): (cubic cm / s)
h = 50       # Initial height (cm)
k = 1.0     # outflow rate constant

# GRAPH
graph = ezGraph(xmax=100, 
                xLabel="Time (s)", yLabel="Height (cm)")
graph.add(0, h)             # add initial values


# TIME LOOP
for t in range(1, nsteps):
    modelTime = t * dt

    # Filling
    dh = Q * dt / (np.pi * r**2)    # find the change in height
    h = h + dh                      # update height

    # Draining
    dVdt = -k * h
    dh = dVdt * dt / (np.pi * r**2)
    h = h + dh
    
    print(modelTime, h)
    graph.add(modelTime, h)
    graph.wait(0.1)

# DRAW GRAPH
graph.keepOpen()
    
