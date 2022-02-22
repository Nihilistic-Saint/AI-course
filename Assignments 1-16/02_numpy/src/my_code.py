import numpy as np
from numpy import save
from numpy import load

# Lue taulukko tiedostosta a.npy ja aseta siin¨a indeksin 0, 0 arvo 1
# ja oikeaan alakulmaan arvo -1. Talleta muokattu taulukko tiedostoon b.npy.

arr = np.load("a.npy")

arr[2, -1:] = -1
print(arr)
save("b.npy", arr)
