import numpy as np
_a = [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ]
a = np.array(_a)
print(np.sum(a, 0))
print(np.max(a))
print(np.min(a, 1))
