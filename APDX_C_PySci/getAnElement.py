import numpy as np


a = np.arange(10)
print(a[7])

print(a[-1])

a.shape = (2, 5)
print(a)

print(a[1, 2])

print(a[0, 2])

print(a[-1, :3])

a[:, 2:4] = 1000
print(a)
