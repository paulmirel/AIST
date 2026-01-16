import numpy as np
from tifffile import imread


cube_filename = '../AIST_data_files/paul_use_these_CASALS_calibration/P7INT_3LAMPS/sessionCAL_000_034_snapshot_cube.tiff'
#cube_filename = '../AIST_data_files/paul_use_these_CASALS_calibration/P5INT_3LAMPS/sessionCAL_000_035_snapshot_cube.tiff'
data_cube_array = imread(cube_filename)
print(data_cube_array.shape)
print(data_cube_array.dtype)
max_possible = 65535 #unit16
max_value = np.max(data_cube_array)
# check for saturation
saturated = (max_value > max_possible - 1) 
print("Saturated =", saturated)
print("max_value =",max_value)
fraction_of_dynamic_range = round(max_value/max_possible, 3)
print("fraction_of_dynamic_range =",fraction_of_dynamic_range)

