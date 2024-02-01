import numpy
import matplotlib.pyplot as plt 

## speed = [2,4,6,1,4,8,7,0,3]

x = numpy.random.normal(5.0, 1.0, 100000)

plt.hist(x, 100)
plt.show()


