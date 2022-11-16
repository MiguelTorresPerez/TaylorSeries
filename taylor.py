# !pip install mpmath
from mpmath import *
def tylor(x):
    return nsum(lambda n: x**n/fac(n), [0, inf])

tylor(1j*math.pi) 
tylor(1)
