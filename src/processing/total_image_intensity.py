import numpy as np


def intensity_array_from_stack(stack):
    """
    Given image stack, returns a list of the total image intensity for each slice.
    """

    total_intensity_array = []
    number_slices =len(stack)

    for slice in range(0, number_slices):
        total_intensity = np.sum(stack[slice])
        total_intensity_array.append(total_intensity)

    return total_intensity_array
