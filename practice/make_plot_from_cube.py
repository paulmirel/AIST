import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from tifffile import imread
import csv

def main(): 
    wavelengths_nm = get_wavelength_list()
    input_folder = '../AIST_data_files/paul_use_these_CASALS_calibration/2026_January_PreBuffalo-AIST-Wavelength+Scene-Data/Argon Lamp/20260122_Argon_000/'
    input_filename = '20260122_Argon_000_008_snapshot_cube.tiff'
    input_cube = imread(Path(input_folder, input_filename))
    x_count, y_count, z_count = input_cube.shape

    layers = np.unstack( input_cube, axis = 2)
    vmax = []
    wl = []
    for band_number in range(0,z_count):
        wl.append(wavelengths_nm[band_number])
        vmax.append(np.max(layers[band_number]))

    fig, ax = plt.subplots()
    ax.plot(wl, vmax)
  
    ax.set(xlabel='wavelength (nm)', ylabel='max value (counts)',
        title='emission line source: Ar')
    ax.grid()

    #fig.savefig("test.png")
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