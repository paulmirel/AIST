#software path prototype

import numpy
from PIL import Image

random_array = numpy.random.rand(40, 40, 10)

nonzero_random_array = numpy.empty_like(random_array)

def make_nonzero( value ): 
    return int(65535*(value+0.1)/10)

x_count, y_count, z_count = random_array.shape
for n in range (0, z_count):
    for x in range(0, x_count):
	    for y in range (0,y_count):
		    nonzero_random_array[x, y, n] = make_nonzero(random_array[ x, y, n])

image_arrays = numpy.unstack( nonzero_random_array, axis = 2 )
print(image_arrays[0])
print(image_arrays[0][0,1])

if False: 
    images = []
    for n in range (0, z_count): 
        images.append(Image.open(image_arrays[n]))