import numpy as np 
def chebyshev_distance(p1, p2):
   return np.max(np.abs(p1-p2))

# Example usage
point1 = np.array([1, 2])
point2 = np.array([3, 4])
print("Chebyshev Distance:", chebyshev_distance(point1, point2))