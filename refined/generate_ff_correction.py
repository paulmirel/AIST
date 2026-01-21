import numpy as np
from pathlib import Path
from tifffile import imread
import csv

def main(): 
    input_folder = '../AIST_data_files/paul_use_these_CASALS_calibration/P7INT_3LAMPS/'
    input_filename = 'sessionCAL_000_034_snapshot_cube.tiff'
    input_cube = imread(Path(input_folder, input_filename))
    x_count, y_count, z_count = input_cube.shape
    if input_cube.shape == (410,410,164): print("data input is the correct shape:", input_cube.shape)
    else: print("data input failed: wrong shape")
    print(input_cube.dtype)

    # check for saturation
    max_possible = 65535 #unit16
    max_value = np.max(input_cube)
    dynamic_range_fraction = round(max_value/max_possible,3)
    if max_value > max_possible - 1: print( "Data contains saturated pixels. Select a different input file.")
    else: print("dynamic_range_fraction =", dynamic_range_fraction)

    wavelengths_nm = get_wavelength_list()
    #print(wavelengths_nm)

    # find the center pixels average value for each band
    center_pixels_radius = 20 
    xy_pixel_count = 410
    center_address = xy_pixel_count/2
    expected_count = int(3.14*center_pixels_radius**2)

    center_spot_average_per_band = []
    for z in range (0, z_count): 
        center_pixels_count = 0 
        spot_values = []
        for x in range(0, x_count):
            for y in range(0, y_count):
                if (x-center_address)**2 + (y-center_address)**2 <= center_pixels_radius**2:
                    center_pixels_count+=1
                    value = input_cube[x][y][z]
                    spot_values.append( value )
        spot_average_value = np.average(spot_values)
        print("band",z,"average value =", int(round(spot_average_value,0)), " Counted", center_pixels_count, "pixels, expected", expected_count)
        center_spot_average_per_band.append(spot_average_value)











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