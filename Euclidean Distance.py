import numpy as np

def euclidean_distance(p1, p2):
  return np.sqrt(np.sum((p1 - p2) ** 2))

# Example usage
point1 = np.array([1, 2])
point2 = np.array([3, 4])
print("Euclidean distance:", euclidean_distance(point1, point2))
