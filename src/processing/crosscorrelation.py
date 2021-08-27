
import numpy as np
import matplotlib.pyplot as plt

from src.processing.radial import create_radius_select_stack


def crosscorrelation_0_to_j(image_stack, start_slice, stop_slice, x_centres, y_centres, radius, plot=False):
    """
    Calculates the crosscorrelation between one slice and a given number of adjacent slices within a
    given stack, created using the 'create_radius_select_stack' function, and plots.

    x_centres and y_centres are 1D arrays/lists of the (x,y) centre coords for each timestamp.
    """
    image_array = image_stack[start_slice:stop_slice]
    x_centre_array, y_centre_array = x_centres[start_slice:stop_slice], y_centres[start_slice:stop_slice]
    x_centre, y_centre = np.mean(x_centre_array), np.mean(y_centre_array)

    stack_list = []
    for i in range(len(image_array)):
        coord_stack = create_radius_select_stack(image_array[i], (x_centre, y_centre), radius, 0.5)
        data = coord_stack[2]
        stack_list.append(data)

    crosscorrelation_list = []
    slice_separation = []
    for j in range(len(stack_list)):
        slice_separation.append(j)
        crosscorrelation = np.corrcoef(stack_list[0], stack_list[j])[0,1]
        crosscorrelation_list.append(crosscorrelation)

    if plot==True:
        plt.figure(figsize = [20,10])
        plt.plot(slice_separation, crosscorrelation_list)

    return slice_separation, crosscorrelation_list