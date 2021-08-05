import math
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FormatStrFormatter
from matplotlib.widgets import Button, Slider
from scipy.ndimage.filters import gaussian_filter

from src.processing.total_image_intensity import *
from src.processing.txt_loading import txt_to_list


def plot_radius_vs_intensity():
    timestamps_n, radii_n, x_centre_n, y_centre_n = txt_to_list('200920_normallight_fitted_circle_position_data.txt')
    timestamps_b, radii_b, x_centre_b, y_centre_b = txt_to_list('200920_biolight_fitted_circle_position_data.txt')
    print('no time intervals= ',len(timestamps_b))
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


    radii_b = np.array(radii_b)
    radii_n = np.array(radii_n)
#raw_intensities_b = np.array(intensity_array_from_stack('200920_biolight_orginal.tif'))
    raw_intensities_b = np.array(intensity_array_from_stack('C:/Cambridge/Mechanics_of_biofilm/algorithm for clear images/biolight_gb_enhance.tif'))
    raw_intensities_n = np.array(intensity_array_from_stack('C:/Cambridge/Mechanics_of_biofilm/algorithm for clear images/normallight_edge_gb.tif'))
    normalized_intensities_b = raw_intensities_b/(math.pi*2*radii_b**2)
    normalized_intensities_n = raw_intensities_n/(math.pi*2*radii_n**2)
    plt.plot(timestamps_b, normalized_intensities_b, label='bioluminescence', marker='o')
    #plt.plot(timestamps_n, normalized_intensities_n, label='brightfield')
    plt.legend()
    plt.xlabel('Time (s)')
    plt.ylabel('Normalized intensity')
    plt.show()

#plot_radius_vs_intensity()


#timestamps_n, radii_n, x_centre_n, y_centre_n = txt_to_list('200920_normallight_fitted_circle_position_data.txt')[0]
#print(timestamps_n)




# timestamps_n, radii_n, x_centre_n, y_centre_n = txt_to_list('200920_normallight_fitted_circle_position_data.txt')
# timestamps_b, radii_b, x_centre_b, y_centre_b = txt_to_list('200920_biolight_fitted_circle_position_data.txt')
# timestamps_b = np.array(timestamps_b) * 1.403726708
# print(len(timestamps_n))
# print(len(timestamps_b))
# plt.plot(timestamps_n, radii_n, label='brightfield')
# plt.plot(timestamps_b, radii_b, label='bioluminescence')
# plt.legend()
# plt.xlabel('Timestamp')
# plt.ylabel('Fitted radius')
# plt.show()

# print('\n')