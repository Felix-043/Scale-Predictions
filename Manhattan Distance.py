import numpy as np 

def manhattan_distance(p1, p2):
  return np.sum(np.abs(p1 - p2))

# Exercise usage
point1 = np.array([1, 2])
point2 = np.array([3, 4])
print("Manhattan distance:", manhattan_distance(point1, point2))