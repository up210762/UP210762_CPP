import numpy as np
import math

def G2R(a):
    r = a * np.pi/180
    return r

def seno(a):
    return math.sin(G2R(a))

a = 45

print(seno(a))
