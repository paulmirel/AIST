import numpy as np
from pathlib import Path
from tifffile import imread
import csv
import matplotlib.pyplot as plt
from matplotlib import colormaps

def main(): 
    wavelengths_nm = get_wavelength_list()

    self_check = True
    if self_check: 
        input_folder = '../AIST_data_files/paul_use_these_CASALS_calibration/P7INT_3LAMPS/'
        input_filename = 'sessionCAL_000_034_snapshot_cube.tiff'
    else: 
        input_folder = '../AIST_data_files/paul_use_these_CASALS_calibration/P5INT_3LAMPS/'
        input_filename = 'sessionCAL_000_035_snapshot_cube.tiff'

    input_cube = imread(Path(input_folder, input_filename))
    x_count, y_count, z_count = input_cube.shape

    # go on to generate witness images, at least one, for band 50 = 550nm
    band = 50
    arrays_2d = np.unstack( input_cube, axis = 2) 
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