import sys
import matplotlib.pyplot as plt
import numpy as np
import math
from matplotlib import cm
A = 1
r1 = 3
r2 = 6
fre = 1
l = 3
def maxR(r1,r2):
    if( r1 > r2):
        return r1
    else:
        return r2
def minR(r1,r2):
    if( r1 < r2):
        return r1
    else:
        return r2
def f(t):
    if(t <=minR(r1,r2)/(l*fre)):
            return 0
    elif (t >= maxR(r1,r2)/l*fre):
            return 2 * A * np.cos(2*np.pi*(r1-r2)/(2*l)) * np.sin((2*np.pi*fre*t) - (2*np.pi*(r1-r2))/(2*l))
    else:
            return A * np.sin(2*np.pi*fre*t - 2*np.pi*minR(r1,r2))

max_t = 10

X = []
Y = []

def addPoint(x1,A):
    A.append(float(x1))
    ##print(x1)
for x in np.arange(0, max_t, 0.002):
        addPoint(f(x),Y)
        addPoint(x,X)
plt.plot(X, Y)
plt.show()
