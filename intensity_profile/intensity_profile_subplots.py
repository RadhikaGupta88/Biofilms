###
# intensity_profile_subplots.py
#
# This script takes in two images of the same biofilm, but one image bl_img
# is taken without a brightfield and shows the bioluminescence of the biofilm,
# while bf_img is taken with a brightfield.
#
# It returns an interactive matplotlib image which picks out a row of the image
# and plots the light intensity along the row for both images on one subplot,
# while showing the row being plotted on an image of the bioluminescent image.
# A slider allows the row to be selected by user.
###

"""
Dependencies
"""
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Button, Slider
from scipy.ndimage.filters import gaussian_filter

"""
Functions
"""
def val_update(val):
    """
    Updates the row we are looking at upon changes of the slider position
    :param val: Value passed from Slider widget, giving the current row
    """
    row = int(row_slider.val) # row_slider.val is a float, so needs converting
    bio_plot.set_ydata(bl_img[row])
    bright_plot.set_ydata(bf_img[row])
    line.set_ydata([row]*columns)
    plt.draw()

"""
Script
"""

# Read in images for bioluminescent and brightfield, and apply gaussian blur
bl_img = mpimg.imread('adjusted biolum.jpg')
bl_img = gaussian_filter(bl_img, sigma=7)

bf_img = mpimg.imread('adjusted brightfield.jpg')
bf_img = gaussian_filter(bf_img, sigma=7)

# Read in parameters of the image. Both are 1388x1040
rows, columns = np.shape(bl_img)

# Create axes
fig, (ax1, ax2) = plt.subplots(1,2)
plt.subplots_adjust(left = 0.1, bottom = 0.35)

# Subplot 1
initial_row = 500
bio_plot, = ax1.plot(bl_img[initial_row], label='bioluminescence')
bright_plot, = ax1.plot(bf_img[initial_row], label='brightfield')
ax1.set_xlabel('Column')
ax1.set_ylabel('Pixel intensity')
ax1.set_title('Intensity profile')
ax1.legend()

# Subplot 2
ax2.imshow(bf_img)
line, = ax2.plot([initial_row]*columns, color='r', linestyle='-')
ax2.set_title('Brightfield image')

# Slider
axSlider = plt.axes([0.1, 0.2, 0.8, 0.05])
row_slider = Slider(axSlider, 'row', valmin=1, valmax=1039, valstep=1)
row_slider.on_changed(val_update)

plt.show()