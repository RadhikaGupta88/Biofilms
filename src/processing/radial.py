import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

def radial_select(image, center, target_radius, tolerance=1.):
    """
    Returns the (x, y) coords and pixel values of a circle taken from a given image at a set target radius.
    """
    y, x = np.indices((image.shape))
    pixel_radius = np.sqrt((x - center[0])**2 
                           + (y - center[1])**2
                          )  # calculate radii of all pixels from center (shape is same as data)
    
    pixel_in_disk = np.logical_and(target_radius - tolerance <= pixel_radius, 
                               pixel_radius <= target_radius + tolerance)
    
    disk_y_coords, disk_x_coords = np.where(pixel_in_disk)
    disk_values = image[disk_y_coords, disk_x_coords]
    
    return disk_y_coords, disk_x_coords, disk_values


def order_coords(disk_y_coords, disk_x_coords, disk_values, center):
    """
    Input: circle's (x, y) coords and values and biofilm center
    Output: stack of (x, y) coords, pixel vals and phi values sorted by angle around circle
    """
    disk_phi_coords = (np.arctan2(disk_y_coords - center[1], disk_x_coords - center[0]))
    stack = np.vstack([disk_x_coords, disk_y_coords, disk_values, disk_phi_coords])
    sorted_stack = stack[:,stack[3,:].argsort()]
    return sorted_stack


def create_radius_select_stack(image, center_fitted, target_radius, tolerance=0.5):
    """
    Uses previous two functions...
    Input: image, centre of biofilm, radius for selection, tolerance
    Output: an array consisting of 4 rows
            row 1 - x coords of selected circle
            row 2 - y coords of selected circle
            row 3 - pixel values of selected circle
            row 4 - phi values of selected circle - angle between point and positive x axis
    """
    disk_x_y_vals = np.array(radial_select(image, center_fitted, target_radius, tolerance))
    stack = order_coords(disk_x_y_vals[0], disk_x_y_vals[1], disk_x_y_vals[2], center_fitted)
    return stack




# finding the period from second highest peak of autocorrelation graph
# function not in use - left here for reference
def find_period_radial_select(stack, plot=False):
    data = stack[2]
    auto_correlation = np.correlate(data, data, mode='same')
    lags = np.arange(-len(auto_correlation)/2, len(auto_correlation)/2)

    peaks, _ = find_peaks(auto_correlation, height=0)
    second_maximum = np.sort(auto_correlation[peaks])[-2]
    index = np.where(auto_correlation == second_maximum)[0]
    period = lags[index[1]]

    if plot == True:
        plt.figure(figsize=(20, 10), dpi=80)
        plt.plot(lags, auto_correlation)
        plt.plot(lags[peaks], auto_correlation[peaks], "x")
        plt.show()
    return period
