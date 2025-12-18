#software path prototype

import numpy
from PIL import Image

random_array = numpy.random.rand(40, 40, 10)

binary_image_array = numpy. dtype=np.uint32)
print(nonzero_random_array.dtype)

def make_nonzero( value ): 
    return bin(int(65535^2*(value+0.1)/10))

x_count, y_count, z_count = random_array.shape
for n in range (0, z_count):
    for x in range(0, x_count):
	    for y in range (0,y_count):
		    nonzero_random_array[x, y, n] = make_nonzero(random_array[ x, y, n])

image_arrays = numpy.unstack( nonzero_random_array, axis = 2 )
print(image_arrays[0])


if False: 
    images = []
    for n in range (0, z_count): 
        images.append(Image.open(image_arrays[n]))