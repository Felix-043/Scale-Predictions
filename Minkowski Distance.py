import numpy as np 

def minkowski_distance(p1, p2, r):
  return np.power(np.sum(np.power(np.abs(p1-p2), r)), 1/r)

# Example usage
point1= np.array([1, 2])
point2 = np.array([3, 4])
print("Minkowski Distance:", minkowski_distance(point1, point2, 3))

  