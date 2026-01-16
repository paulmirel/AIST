import numpy as np
from tifffile import imread
import matplotlib.pyplot as plt
from matplotlib import colormaps
import csv


cube_filename = '../AIST_data_files/paul_use_these_CASALS_calibration/P7INT_3LAMPS/sessionCAL_000_034_snapshot_cube.tiff'
#cube_filename = '../AIST_data_files/paul_use_these_CASALS_calibration/P5INT_3LAMPS/sessionCAL_000_035_snapshot_cube.tiff'
data_cube_array = imread(cube_filename)
print(data_cube_array.shape)
print(data_cube_array.dtype)
max_possible = 65535 #unit16
max_value = np.max(data_cube_array)
#print(np.histogram(data_cube_array))

# check for saturation
saturated = (max_value > max_possible - 1) 
print("Saturated =", saturated)
print("max_value =",max_value)
fraction_of_dynamic_range = round(max_value/max_possible, 3)
print("fraction_of_dynamic_range =",fraction_of_dynamic_range)

# unstack the data cube
one_array_per_band = np.unstack(data_cube_array, axis = 2)

# pull in the wavelength bands list
with open('../AIST_data_files/Cubert_Ultris_VNIR_spectral_bands.csv', newline='') as csv_band_list:
    band_tuples = list(csv.reader(csv_band_list))
band_tuples.pop(0)
wavelengths_nm = []
for tuple in band_tuples: 
    wavelengths_nm.append(int(tuple[1]))
#print(wavelengths_nm)


# find the center pixels average value for each band
center_pixels_radius = 20 
pixel_count = 410
center_address = pixel_count/2

center_average_values = []
for index in range (0, len(one_array_per_band)): 
    center_pixels_count = 0 
    value_list = []
    for x in range(0, pixel_count):
        for y in range(0, pixel_count):
            #if x**2 + y**2 <= center_pixels_radius**2: #from the corner!!
            if (x-center_address)**2 + (y-center_address)**2 <= center_pixels_radius**2:
                center_pixels_count+=1
                value = one_array_per_band[index][x][y]
                #print( x, y, value )
                value_list.append( value )
    center_average_value = np.average(value_list)
    
    center_average_values.append(center_average_value)
    #print( "radius =", center_pixels_radius )
    #print( "pixels in center =", center_pixels_count )
    #print( "expected pixels =", 3.14*center_pixels_radius**2)
    #print( "wavelength", wavelengths_nm[index],"nm", "average value =", center_average_value)

for index in range (0, len(one_array_per_band)): 
    print(wavelengths_nm[index],center_average_values[index])