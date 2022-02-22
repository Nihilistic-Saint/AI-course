#Lue tiedosto ab.npz ja talleta taulukko,
# jonka nimi on b tiedostoon b2.npy.
import numpy as np
from numpy import save
from numpy import savez
from numpy import load
    
ab = np.load("ab.npz")

barr = ab['b']
save("b2.npy", barr)
print(barr)