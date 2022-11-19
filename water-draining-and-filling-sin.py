import numpy as np 
import time 
from ezGraph import *
from uStats import * 

# Finite Difference Model

startTime = time.perf_counter()

# PARAMETERS
dt = 1          # timestep
nsteps = 100   # number of timesteps

r = 2.25    # radius (cm)
Qin = 30       # Volume inflow rate (dV/dt): (cubic cm / s)
h = 0       # Initial height (cm)
k = 0.15     # outflow rate constant
dQ = -0.1

# EXPERIMENTAL DATA
y_modeled = []

# GRAPH
graph = ezGraph(xmin=0, xmax=100, 
                xLabel="Time (s)", 
                yLabel="Height (cm)")

graph.add(0, h)   # add initial values

Qflag = True

# TIME LOOP
for t in range(1, nsteps):
    modelTime = t * dt

    # if (modelTime <= 5) or (modelTime >10 and modelTime < 15) or (modelTime>20 and modelTime<=25):
    #     Qin = 30
    # else:
    #     Qin = 0

    Qin = 10 * np.sin(50*modelTime) + 11

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

    # find max
    if t > 2:
        if (graph.y[-2] > graph.y[-1]) and (graph.y[-2] > graph.y[-3]):
            print(f"Max: {graph.y[-2]}")
        if (graph.y[-2] < graph.y[-1]) and (graph.y[-2] < graph.y[-3]):
            print(f"Min: {graph.y[-2]}")

    if t > 1:
        dh = graph.y[-1] - graph.y[-2]
        dh_old = graph.y[-2] - graph.y[-3]
        if (dh < 0) and (dh_old > 0):
            print(f"Max dh: {graph.y[-2]}")

print(f"Max (John): {max(graph.y)}")

endTime = time.perf_counter()

runtime = endTime - startTime
print(f'runtime: {runtime}')

# DRAW GRAPH
graph.keepOpen()
    
