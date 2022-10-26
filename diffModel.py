import numpy as np
import time
from ezGraph import *

n = 10

tsteps = 500
dt = 0.1

dx = 1
T = np.ones((n,)) * 5

# boundary conditions
T[0] = 5
T[n-1] = 10

K = 0.1
A = 1

V = A * dx

# SET UP GRAPH
graph = ezGraph()
graph.plot(T)
graph.wait(1)
print(f"-1: T")


for t in range(tsteps):
    Qin = -K * A * (T[1:-1] - T[:-2]) / dx
    Qout = K * A * (T[2:] - T[1:-1]) / dx   
    T[1:-1] += Qin + Qout

    if (t%10 == 0):
        
        graph.updatePlot(T, dt=0.1, title=f"{t+1}/{tsteps}")
    

# DRAW GRAPH
graph.updatePlot(T, dt=0.1, title=f"{t+1}/{tsteps}")       # final update
graph.keepOpen()    # keep graph open when done
