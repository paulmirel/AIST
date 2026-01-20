import numpy as np
from tifffile import imread
import matplotlib.pyplot as plt
from matplotlib import colormaps

filepath = '../AIST_data_files/flat_field_correction_cube.npy'
ff_correction_cube = np.load(filepath)
print( ff_correction_cube.shape)
print( ff_correction_cube.dtype)

cube_filename = '../AIST_data_files/paul_use_these_CASALS_calibration/P7INT_3LAMPS/sessionCAL_000_034_snapshot_cube.tiff'
#cube_filename = '../AIST_data_files/paul_use_these_CASALS_calibration/P5INT_3LAMPS/sessionCAL_000_035_snapshot_cube.tiff'
data_cube_array = imread(cube_filename)
print(data_cube_array.shape)
print(data_cube_array.dtype)




