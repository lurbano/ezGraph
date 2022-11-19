import numpy as np 
import time 
from ezGraph import *
from uStats import * 

# Finite Difference Model

startTime = time.perf_counter()

# PARAMETERS
dt = 5          # timestep
nsteps = 200    # number of timesteps

r = 2.25    # radius (cm)
Qin = 30       # Volume inflow rate (dV/dt): (cubic cm / s)
h = 0       # Initial height (cm)
k = 0.15     # outflow rate constant

# EXPERIMENTAL DATA
y_modeled = []

# GRAPH
graph = ezGraph(xmin=0, xmax=100, 
                xLabel="Time (s)", 
                yLabel="Height (cm)")

graph.add(0, h)   # add initial values

# TIME LOOP
for t in range(1, nsteps):
    modelTime = t * dt

    # Filling
    dh = Qin * dt / (np.pi * r**2)  # find the change in height
    h = h + dh                      # update height

    # Draining
    dVdt = -k * h
    dh = dVdt * dt / (np.pi * r**2)
    h = h + dh
    
    # save height (h) calculated by the model
    #  only if the model time corresponds to one
    #  of the times when a measurement was taken
    
    graph.add(modelTime, h)
    #graph.wait(0.01)


endTime = time.perf_counter()

runtime = endTime - startTime
print(f'runtime: {runtime}')

# DRAW GRAPH
graph.keepOpen()
    
