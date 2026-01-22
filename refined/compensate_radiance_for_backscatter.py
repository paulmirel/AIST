import numpy as np
from pathlib import Path

print("Ultris bandwidth is 10nm FWHM for each channel")
print("What is the bandwidth of the Ultris, and of the ASD?")
# import the asd files, direct view and monitor
# average them
# compensate for backscatter
# save compensated files
input_folder = '../AIST_data_files/paul_use_these_CASALS_calibration/ASD with Direct View of Sphere (treated as unloaded sphere)/'
input_filename = 'CASALS_1L_DirectView00000.asd.txt'
with open(Path(input_folder, input_filename), 'r') as fp:
    x = fp.readlines()[690:695]#[40:691]
    print(x)


## figure out a method to combine bands, get it workiing, and then run it past Jesse