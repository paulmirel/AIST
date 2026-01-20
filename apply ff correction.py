import numpy as np
from tifffile import imread, imwrite
import matplotlib.pyplot as plt
from matplotlib import colormaps
from PIL import Image
import time

filepath = '../AIST_data_files/flat_field_correction_cube.npy'
ff_correction_cube = np.load(filepath)
print( ff_correction_cube.shape)
print( ff_correction_cube.dtype)

cube_filepath = '../AIST_data_files/paul_use_these_CASALS_calibration/P7INT_3LAMPS/sessionCAL_000_034_snapshot_cube.tiff'
#cube_filepath = '../AIST_data_files/paul_use_these_CASALS_calibration/P5INT_3LAMPS/sessionCAL_000_035_snapshot_cube.tiff'
data_cube_array = imread(cube_filepath)
x_count, y_count, z_count = data_cube_array.shape
print(z_count)
print(data_cube_array.shape)
print(data_cube_array.dtype)
data_ff_corrected = np.zeros_like(data_cube_array)

start = time.monotonic()
print("working ...")
for z in range (0, z_count): 
    print("layer", z)
    for x in range (0, x_count): 
        for y in range (0, y_count): 
            new_value_float = ff_correction_cube[x][y][z] * data_cube_array[x][y][z]
            data_ff_corrected[x][y][z] = int(round(new_value_float, 0))
            #print( x, y, z, data_ff_corrected[x][y][z], new_value_float, ff_correction_cube[x][y][z],  data_cube_array[x][y][z])
stop = time.monotonic()
elapsed = round(stop - start, 1) 
print("elapsed", elapsed, "s")
print(data_ff_corrected.shape)
if False: 
    filepath = '../AIST_data_files/P7INT_3LAMPS_sessionCAL_000_034_ffcorrected_cube.tiff'
    try: 
        dataout=Image.fromarray(data_ff_corrected)
        dataout.save(filepath)
    except Exception as err: 
        print("file not saved because ", err)
          


