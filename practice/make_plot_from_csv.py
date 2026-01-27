import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
import csv

input_folder = '../AIST_data_files/'
input_filename = 'Ar_intensity_v_WL.csv'

with open(Path(input_folder, input_filename), newline='') as wl_intensity_pairs:
    wl_tuples = list(csv.reader(wl_intensity_pairs))

wl = []
rel = []
for index in range (0, len(wl_tuples)):
    wl.append(float(wl_tuples[index][0]))
    rel.append(float(wl_tuples[index][1]))

if True: 
    fig, ax = plt.subplots()
    ax.plot(wl, rel)

    ax.set(xlabel='wavelength (nm)', ylabel='relative intensity',
        title='NIST emission line spectrum: Ar')
    ax.grid()

    #fig.savefig("test.png")
    plt.show()