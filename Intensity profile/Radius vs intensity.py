import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from scipy.ndimage.filters import gaussian_filter
import pandas
from matplotlib.widgets import Slider, Button
from matplotlib.ticker import FormatStrFormatter

from total_image_intensity import *

def txt_to_list(name):

    with open('c:/Cambridge/Mechanics of biofilm/George algorithm/Data_Storage/200920/' + str(name)) as f:
        contents = [line.split(',') for line in f]

    rows = len(contents)
    contents = np.array(contents).reshape(rows, 4)
    timestamps = list(np.float_(contents[1:,0]))
    radii = list(np.float_(contents[1:,1]))
    x_centre = list(np.float_(contents[1:,2]))
    y_centre = list(np.float_(contents[1:,3]))

    return timestamps, radii, x_centre, y_centre

timestamps_n, radii_n, x_centre_n, y_centre_n = txt_to_list('200920_normallight_fitted_circle_position_data.txt')
timestamps_b, radii_b, x_centre_b, y_centre_b = txt_to_list('200920_biolight_fitted_circle_position_data.txt')
#plt.plot(timestamps,radii)
#fig, ax = plt.subplots()
#plt.xticks(np.arange(0, 6, 0.5))
#plt.yticks(np.arange(200, 610, 100))
# ax.xaxis.set_major_formatter(FormatStrFormatter('%.1f'))
# ax.xaxis.set_ticks(np.arange(0,5.5,0.5))
#
# print(len(timestamps_b))
# plt.plot(timestamps_n, radii_n, label='Brightfield')
# plt.plot(timestamps_b, radii_b, label='Bioluminescence')
# plt.xlabel('Time (s)')
# plt.ylabel('Fitted radius (10s of nm)')
# plt.legend()
# plt.show()

radii_b = np.array(radii_b)
raw_intensities_b = np.array(intensity_array_from_stack('200920_biolight_orginal.tif'))
normalized_intensities_b = raw_intensities_b/(radii_b**2)
plt.plot(timestamps_b, normalized_intensities_b)
plt.xlabel('Time (s)')
plt.show()