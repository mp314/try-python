import numpy as np
from numpy.random import default_rng



def transpose(d):
  return d.T

rng = default_rng()
vals = rng.standard_normal(10)
more_vals = rng.standard_normal(10)
#print("Vals", vals)
#print("More vals", more_vals)
a = np.zeros((10, 2))
a = np.array([vals,more_vals])
print("a ", a.shape)

# A transpose makes the array non-contiguous
#b = a.T
b = transpose(a)
print("b ",b.shape)

c = b.view()

print("c ",c)