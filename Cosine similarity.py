from scipy.spatial import distance
import numpy as np

def cosine_similarity(p1, p2):
  return 1 - distance.cosine(p1, p2)

# Example usage
point1 = np.array([1, 2])
point2 = np.array([3, 4])
print("cosine similarity:", cosine_similarity(point1, point2))