import numpy as np
from pathlib import Path
from tifffile import imread

input_folder = '../AIST_data_files/paul_use_these_CASALS_calibration/P7INT_3LAMPS/'
input_filename = 'sessionCAL_000_034_snapshot_cube.tiff'
input_cube = imread(Path(input_folder, input_filename))
print(input_cube.shape)
if input_cube.shape == (410,410,164): print("data input is the correct shape")
else: print("data input failed: wrong shape")
print(input_cube.dtype)

# check for saturation
max_possible = 65535 #unit16
max_value = np.max(input_cube)
dynamic_range_fraction = round(max_value/max_possible,3)
if max_value > max_possible - 1: print( "Data contains saturated pixels. Select a different input file.")
else: print("dynamic_range_fraction =", dynamic_range_fraction)