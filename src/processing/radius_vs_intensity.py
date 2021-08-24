import math
import matplotlib.pyplot as plt
import numpy as np

from src.processing.total_image_intensity import intensity_array_from_stack
from src.processing.txt_loading import txt_to_list


def plot_radius_vs_intensity(bio_stack, normallight_stack):

    """
    Plot biofilm image intensity normalized by biofilm area, against biofilm radius.
    """

    timestamps_n, radii_n, x_centre_n, y_centre_n = txt_to_list('200920_normallight_fitted_circle_position_data.txt')
    timestamps_b, radii_b, x_centre_b, y_centre_b = txt_to_list('200920_biolight_fitted_circle_position_data.txt')
    print('no time intervals biolight= ',len(timestamps_b))
    print('no time intervals nromallight= ',len(timestamps_n))

    radii_b = np.array(radii_b)
    radii_n = np.array(radii_n)

    plt.figure(figsize=(20,10))

    #get image intensities
    raw_intensities_b = np.array(intensity_array_from_stack(bio_stack))
    normalized_intensities_b = raw_intensities_b/(math.pi*2*radii_b**2)
    plt.plot(radii_b, normalized_intensities_b, label='bioluminescence', marker='o')

    if normallight_stack != None:
        raw_intensities_n = np.array(intensity_array_from_stack(normallight_stack))
        normalized_intensities_n = raw_intensities_n/(math.pi*2*radii_n**2)
        plt.plot(radii_n, normalized_intensities_n, label='brightfield', marker='o')



    plt.legend()
    plt.xlabel('Biofilm radius (pixels)')
    plt.ylabel('Area-normalized intensity')
    plt.show()
