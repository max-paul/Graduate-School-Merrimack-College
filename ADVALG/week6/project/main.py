from simplex import simplex
import numpy as np
# Objective function weights
c = np.array([3, 2, 2])

# Constraints matrix
A = np.array([[2, 4, 5], [1, 2, 4], [8, 0, 3]])

# Constraints right-hand side values
b = np.array([300, 200, 300])
x, obj = simplex(c, A, b)

print("Optimal solution:", x)
print("Optimal objective value:", obj)