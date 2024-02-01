import numpy as np

ages = [23,56,87,45,75,36,76,24,11,42,73]

x = np.percentile(ages, 75)
y = np.percentile(ages, 50)
z = np.percentile(ages, 25)
print(x)
print(y)
print(z)