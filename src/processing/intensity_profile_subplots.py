<<<<<<< HEAD
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
from src.processing.constants import BUCKLING_PATH, MECHANICS_OF_BIOFILM_PATH
=======
>>>>>>> main
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Slider
from scipy.ndimage.filters import gaussian_filter
from skimage.io import imread
from src.processing.constants import BUCKLING_PATH

"""
Constants
"""
path_to_bl_img = 'c:/Cambridge/Mechanics_of_biofilm/algorithm for clear images/200920_biolight_nobg_nooutliers_despeckle_enhance.tif'
path_to_bm_img = 'c:/Cambridge/Mechanics_of_biofilm/algorithm for clear images/200920_normallight_nobg_edges_gaussblur_enhance.tif'

<<<<<<< HEAD
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
=======
def access_row_data(biolum,bright,row,low=0, high=1388):

    if len(np.shape(biolum)) == 3: #if mulitchannel data
        bio_data = biolum[row, :, 0]
        bright_data = bright[row, :, 0]
        integers = list(range(1, len(bio_data)+1))

    if len(np.shape(biolum)) == 2: #if greyscale data
        bio_data = biolum[row, :]
        bright_data = bright[row, :]
        integers = list(range(1, len(bio_data) + 1))
>>>>>>> main

# Read in images for bioluminescent and brightfield, and apply gaussian blur
bl_img = 0.5*imread(path_to_bl_img)[150]
bl_img = gaussian_filter(bl_img, sigma=7)

<<<<<<< HEAD
bf_img = 0.9*imread(path_to_bm_img)[150]
bf_img = gaussian_filter(bf_img, sigma=7)
=======

def intensity_profile_interactive(biolight_img, brightfield_img, gaussian_filter_sigma=None):

    if gaussian_filter_sigma != None:
        biolight_img =  gaussian_filter(biolight_img, sigma=gaussian_filter_sigma)
        brightfield_img =  gaussian_filter(brightfield_img, sigma=gaussian_filter_sigma)

    rows, columns = np.shape(biolight_img)

    #setup figure
    fig, (ax1, ax2) = plt.subplots(1,2)
    fig.set_size_inches(15,10)
    plt.subplots_adjust(left = 0.1, bottom = 0.35)

    #subplot 1
    integers, bio_data, bright_data = access_row_data(biolight_img, brightfield_img, 600)
    bio_plot, = ax1.plot(integers, bio_data, label='bioluminescence')
    bright_plot, = ax1.plot(integers, bright_data, label='brightfield')
    ax1.legend(loc="upper right")
    ax1.set_xlabel('Column')
    ax1.set_ylabel('Pixel intensity')
    ax1.set_title('Intensity profile')

    #interactive slider setup
    axSlider = plt.axes([0.1, 0.2, 0.8, 0.05])
    row_slider = Slider(axSlider, 'row', valmin=1, valmax=1039, valstep=1)

    #subplot 2
    ax2.imshow(brightfield_img)
    line, = ax2.plot(np.zeros(columns), color='r', linestyle='-')
    ax2.set_title('Brightfield image')


    def val_update(val):
        row = row_slider.val
        bio_plot.set_ydata(access_row_data(biolight_img, brightfield_img, row)[1])
        bright_plot.set_ydata(access_row_data(biolight_img, brightfield_img, row)[2])
        line.set_ydata(row)
        plt.draw()

    row_slider.on_changed(val_update)

    plt.show()


bio_stack = imread(str(BUCKLING_PATH / '200920_biolight_nobg_nooutliers_despeckle_enhance.tif'))
bright_stack = imread(str(BUCKLING_PATH / '200920_normallight_nobg_edges_gaussblur_enhance.tif'))

slice_no_bio = 150
STACK_B_TO_N_RATIO = len(bio_stack) / len(bright_stack)
slice_no_bright = int(slice_no_bio / STACK_B_TO_N_RATIO)

intensity_profile_interactive(bio_stack[slice_no_bio], bright_stack[slice_no_bright])


"""
>>>>>>> main

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

<<<<<<< HEAD
plt.show()
=======
plt.title('Intensity profile',  y=14)
plt.show()

<<<<<<< HEAD
>>>>>>> main
=======
"""
>>>>>>> main
