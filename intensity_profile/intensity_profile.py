import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
import pandas
import plotly.express as px
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
height, width = np.shape(bl_img)

# Create axes for the plot
fig, ax = plt.subplots()
plt.subplots_adjust(left = 0.1, bottom = 0.35)
plt.title('Intensity profile')
plt.xlabel('Column')
plt.ylabel('Pixel intensity')

# Make an initial plot, looking at row 500
initial_row = 500
bio_plot, = plt.plot(bl_img[initial_row], label='bioluminescence')
bright_plot, = plt.plot(bf_img[initial_row], label='brightfield')
plt.legend()

# Allow adjusting of the row using Slider widget
axSlider = plt.axes([0.1, 0.2, 0.8, 0.05])
row_slider = Slider(axSlider, 'row', valmin = 0, valmax=height - 1, valstep=1)
row_slider.on_changed(val_update)
plt.show()
