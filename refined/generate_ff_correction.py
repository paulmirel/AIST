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
