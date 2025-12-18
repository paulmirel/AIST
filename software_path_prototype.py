#software path prototype

import numpy as np
import matplotlib.pyplot as plt

ar1 = np.random.rand(410, 410, 10)
ar2 = np.empty_like(ar1)

def make_nonzero( value ): 
    return (value+0.1)/10

x_count, y_count, z_count = ar1.shape
for n in range (0, z_count):
    for x in range(0, x_count):
	    for y in range (0,y_count):
		    ar2[x, y, n] = make_nonzero(ar1[ x, y, n])

ars = np.unstack( ar2, axis = 2) 

r = SQRT((xn - x’)^2 + (yn - y’)^2 ) 

plt.imshow(ars[0], cmap='gray')
plt.colorbar()
plt.show()

