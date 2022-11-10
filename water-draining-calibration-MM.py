import numpy as np 
import time 
from ezGraph import *
from uStats import * 

# Finite Difference Model

# PARAMETERS
dt = 1
nsteps = 160

r = 2.25    # radius (cm)
Qin = 0       # Volume inflow rate (dV/dt): (cubic cm / s)
h = 50       # Initial height (cm)
k = 0.15     # outflow rate constant

# EXPERIMENTAL DATA
x_measured = [0, 28, 60, 101, 157]
y_measured = [50, 40, 30, 20, 10]
y_modeled = [h]

# GRAPH
graph = ezGraphMM(xmin=0, xmax=100, 
                xLabel="Time (s)", 
                yLabel="Height (cm)",
                x_measured = x_measured,
                y_measured = y_measured)

graph.addModeled(0, h)   # add initial values

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
    if (modelTime in x_measured):
        print(modelTime, h)
        y_modeled.append(h)

    graph.addModeled(modelTime, h)
    #graph.wait(0.01)

print("time:", x_measured)
print("h_measured:", y_measured)
print("h_modeled:", y_modeled)

print(f'avg measured = {findAvg(y_measured)}')
# calculate average values for y_measured and y_modeled

print(f'Residuals squared: {resSq(y_measured, y_modeled)}')

print(f'r^2: {rSquared(y_measured, y_modeled)}')
# DRAW GRAPH
graph.keepOpen()
    
