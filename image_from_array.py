import numpy
import matplotlib.pyplot as plt
from matplotlib import colormaps
print(list(colormaps))

ar1 = numpy.random.rand(40, 40, 10)
print(ar1[0,0,0])
ars = numpy.unstack( ar1, axis = 2) 

plt.imshow(ars[0], cmap='gray')
plt.colorbar()
plt.show()


