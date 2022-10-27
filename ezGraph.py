import matplotlib.pyplot as plt
import numpy as np

class ezGraph:
    def __init__(self, xmin=0, xmax=10, ymin="auto", ymax="auto", xLabel="x", yLabel="y"):
        self.x = []          
        self.y = []
        self.fig, self.ax = plt.subplots()    # initialize matplotlib plot
        plt.xlim([xmin, xmax])
        if ymin != "auto" and ymax != "auto":
            plt.ylim([ymin, ymax])
        self.ax.set_xlabel(xLabel)  # label axes
        self.ax.set_ylabel(yLabel)  # label axes
        self.ax.plot(self.x, self.y)               # put data into plot (line)
        self.ax.scatter(self.x, self.y)        

    def add(self, x, y):
        self.x.append(x)
        self.y.append(y) 
        self.ax.plot(self.x, self.y)               # put data into plot
        self.ax.scatter(self.x, self.y)

    def plot(self, y, dx=1):
        self.x = np.ones(y.shape) 
        for i in range(len(self.x)):
            self.x[i] = i * dx
        self.y = y 
        self.ax.plot(self.x, self.y)               # put data into plot
        self.ax.scatter(self.x, self.y)

    def updatePlot(self, y, dt=0.25, title="Plot", dx=1):
        self.clear()
        self.plot(y, dx)
        self.title(title)
        self.wait(dt)



    def wait(self, dt):
        plt.pause(dt)

    def keepOpen(self):
        plt.show()

    def clear(self):
        plt.cla()

    def title(self, txt="Plot"):
        self.ax.set_title(txt)
        