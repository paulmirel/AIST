import numpy as np
from pathlib import Path
from tifffile import imread
from PIL import Image
import csv
import time
import matplotlib.pyplot as plt
from matplotlib import colormaps

def main(): 
    calibration_source_folder = '../AIST_data_files/'
    calibration_filename = 'ultris_ff_cal_p7int_3lamps_session_000_034.npy' 
    ff_correction_cube = np.load(Path(calibration_source_folder, calibration_filename))
    print( ff_correction_cube.shape)
    print( ff_correction_cube.dtype)
    
    self_check = False #True
    if self_check: 
        input_folder = '../AIST_data_files/paul_use_these_CASALS_calibration/P7INT_3LAMPS/'
        input_filename = 'sessionCAL_000_034_snapshot_cube.tiff'
    else: 
        input_folder = '../AIST_data_files/paul_use_these_CASALS_calibration/P5INT_3LAMPS/'
        input_filename = 'sessionCAL_000_035_snapshot_cube.tiff'

    input_cube = imread(Path(input_folder, input_filename))
    x_count, y_count, z_count = input_cube.shape
    if input_cube.shape == (410,410,164): print("input data set is the correct shape:", input_cube.shape)
    else: print("data input failed: wrong shape")
    print(input_cube.dtype)

    # check for saturation
    max_possible = 65535 #unit16
    max_value = np.max(input_cube)
    dynamic_range_fraction = round(max_value/max_possible,3)
    if max_value > max_possible - 1: print( "NOTE: Input data set contains saturated pixels.")
    else: print("dynamic_range_fraction =", dynamic_range_fraction)

    wavelengths_nm = get_wavelength_list()
    #print(wavelengths_nm)

    data_ff_corrected = np.zeros_like(input_cube)

    start = time.monotonic()
    print("working ...")
    for z in range (0, z_count): 
        print("layer", z)
        for x in range (0, x_count): 
            for y in range (0, y_count): 
                new_value_float = ff_correction_cube[x][y][z] * input_cube[x][y][z]
                data_ff_corrected[x][y][z] = int(round(new_value_float, 0))
                #print( x, y, z, data_ff_corrected[x][y][z], new_value_float, ff_correction_cube[x][y][z],  data_cube_array[x][y][z])
    stop = time.monotonic()
    elapsed = round(stop - start, 1) 
    print("elapsed", elapsed, "s")
    max_value = np.max(data_ff_corrected)
    min_value = np.min(data_ff_corrected)
    print("min =", min_value, "max = ", max_value)
    if max_value > max_possible - 1: print( "NOTE: FF corrected data set contains saturated pixels.")
    else: print("FF corrected dynamic range fraction =", dynamic_range_fraction)
    

    output_folder = input_folder
    output_filename = input_filename[:-5]+'_FF_corrected.npy'
    try: 
        np.save(Path(output_folder, output_filename), data_ff_corrected)
        print("flat field corrected data saved as:", output_filename)
    except Exception as err: 
        print("file not saved because ", err)

    if False:   
    # save data_ff_corrected as a tiff
        try: 
            print(data_ff_corrected.shape)
            output_tiff_image = Image.fromarray(data_ff_corrected, mode='F')
            output_folder = '../AIST_data_files/paul_use_these_CASALS_calibration/P7INT_3LAMPS/'
            output_filename = 'sessionCAL_000_034_snapshot_cube_FF_corrected.tiff'
            output_tiff_image.save(Path(output_folder, output_filename))
        except Exception as err: 
            print("failed to save because:", err)

    # go on to generate witness images, at least one, for band 50 = 550nm
    band = 50
    arrays_2d = np.unstack( data_ff_corrected, axis = 2) 
    deviation = round(np.std(arrays_2d[band]),1)
    average_value = round(np.average(arrays_2d[band]),1)
    plt.title('{}nm, value = {}+/-{}'.format(wavelengths_nm[band], average_value, deviation))
    plt.imshow(arrays_2d[band], cmap='gray')
    plt.colorbar()
    plt.show()


def get_wavelength_list(): 
    # pull in the wavelength bands list
    with open('../AIST_data_files/Cubert_Ultris_VNIR_spectral_bands.csv', newline='') as csv_band_list:
        band_tuples = list(csv.reader(csv_band_list))
    band_tuples.pop(0)
    wavelengths_nm = []
    for tuple in band_tuples: 
        wavelengths_nm.append(int(tuple[1]))
    #print(wavelengths_nm)
    return wavelengths_nm

main()



