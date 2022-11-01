import numpy as np 
import time 
from ezGraph import *

# Finite Difference Model of the 
#  Height of a Ballistic Ball

# PARAMETERS
dt = 0.1
nsteps = 45

g = -9.8     # acceleration due to gravity (m/s^2)

# INITIAL VALUES
h = 0       # initial height (m)
v = 20      # initial velocity (m/s)

# GRAPH
graph = ezGraph(xmin=0, xmax=100, 
                xLabel="Time (s)", 
                yLabel="Ball Height (m)")

graph.add(0, h)     # add initial values

# TIME LOOP
for t in range(1, nsteps):
    modelTime = t * dt

    # First find the velocity
    v = v + g * dt   

    # Find new height
    h = h + v * dt
    
    graph.add(modelTime, h)
    graph.wait(0.1)

# DRAW GRAPH
graph.keepOpen()
    
