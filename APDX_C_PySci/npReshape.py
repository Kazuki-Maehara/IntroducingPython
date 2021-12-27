import numpy as np

a = np.arange(10)

print(a)

b = a.reshape(2, 5)

print(b.ndim)
print(b.size)
print(b.shape)


c = a.reshape(5, 2)

print(c)
print(c.ndim)
print(c.size)
print(c.shape)

a.shape = (2, 5)
print(a)
