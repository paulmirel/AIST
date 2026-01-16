#software path prototype

import numpy as np
import matplotlib.pyplot as plt
import math

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

def get_r( x, y ):
    x_center = 200
    y_center = 208
    return math.sqrt((x - x_center)**2 + (y - y_center)**2 ) 

if True: 
    plt.imshow(ars[0], cmap='gray')
    plt.colorbar()
    plt.show()

flar1 = np.empty([x_count, y_count])

for x in range(0, x_count):
	for y in range (0, y_count):
            value = ars[0][ x, y ]
            radius = get_r(x,y)
            flar1[x, y,] = value/radius**4 + value * math.sqrt(radius) - 417 * radius

plt.imshow(flar1, cmap='gray')
plt.colorbar()
plt.show()