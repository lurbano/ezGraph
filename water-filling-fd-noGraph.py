import math
# Finite Difference Model

# PARAMETERS
dt = 1.
nsteps = 20

r = 2.25    # radius (cm)
Q = 5       # Volume inflow rate: (cubic cm / s)
h = 0       # Initial height (cm)

print(0, h)     # print initial values

# TIME LOOP
for t in range(1, nsteps):
    modelTime = t * dt

    dh = Q * dt / (math.pi * r**2)    # find the change in height
    h = h + dh                      # update height
    
    print(modelTime, h)

    
