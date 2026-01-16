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

one_array_per_band = np.unstack(data_cube_array, axis = 2)

with open('../AIST_data_files/Cubert_Ultris_VNIR_spectral_bands.csv', newline='') as csv_band_list:
    band_tuples = list(csv.reader(csv_band_list))

print(band_tuples[1][0], band_tuples[1][1])



for index in range (0, len(one_array_per_band)): 
    print("showing band:", index)
    plt.imshow(one_array_per_band[index], cmap='gray')
    plt.title('Wavelength ' + str(band_tuples[index+1][1])+ "nm")
    plt.colorbar()
    plt.figure(1)
    plt.show()
    plt.pause(1)
    plt.clf()
       
