import numpy as np
from pathlib import Path
from tifffile import imread
import csv
import matplotlib.pyplot as plt
from matplotlib import colormaps

def main(): 
    wavelengths_nm = get_wavelength_list()
    
    input_folder = '../AIST_data_files/paul_use_these_CASALS_calibration/2026_January_PreBuffalo-AIST-Wavelength+Scene-Data/Argon Lamp/20260122_Argon_000/'
    input_filename = '20260122_Argon_000_008_snapshot_cube.tiff'

    input_cube = imread(Path(input_folder, input_filename))
    x_count, y_count, z_count = input_cube.shape

    arrays_2d = np.unstack( input_cube, axis = 2) 
    data_to_plot = []
    for band in range (0, z_count):
        brightest_value = np.max(arrays_2d[band])
        data_to_plot.append( (wavelengths_nm[band], brightest_value) )
    print(data_to_plot)

    plt.plot(data_to_plot)
    plt.show()

    if False: 
        plt.title('{}nm, value = {}+/-{}'.format(wavelengths_nm[band], average_value, deviation))
        plt.imshow(arrays_2d[band], cmap='gray')
        plt.colorbar()
        plt.show()
        plt.pause(1)
        plt.clf()




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