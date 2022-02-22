import numpy as np
from numpy import savez
from numpy import load

"""
Lue taulukot tiedostoista a.npy ja b.npy 
Talleta ne molemmat taulukot tiedostoon ab.npz. 
Tallenna ensimmainen taulukkonimella a 
ja jalkimmainen nimell¨a b.
"""
a = np.load("a.npy")
b = np.load("b.npy")

np.savez('ab.npz',a=a, b=b)

ab = np.load("ab.npz")
print(ab.files)