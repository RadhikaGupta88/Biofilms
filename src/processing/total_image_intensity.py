import matplotlib.pyplot as plt
import numpy as np
from skimage import io


def intensity_array_from_stack(stack):
    image = io.imread(stack)
    total_intensity_array = []
    number_slices = np.shape(image)[0]

    for slice in range(0, number_slices):
        total_intensity = np.sum(image[slice])
        total_intensity_array.append(total_intensity)

    return total_intensity_array
