import numpy as np
from numpy import save
# Luo taulukko a, jossa on 3 rivi¨a ja 4 saraketta ja kaikkien
# alkioiden arvo on 0. Talleta taulukko tiedostoon a.npy.

a = np.zeros((3,4))
print(a)

save('a.npy',a)