import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from scipy.ndimage.filters import gaussian_filter
import pandas
from matplotlib.widgets import Slider, Button

import plotly.express as px


img1 = mpimg.imread('test_biolum.jpg')
img2 = mpimg.imread('test_bright.jpg')

img3 = mpimg.imread('adjusted biolum.jpg')
img3 = gaussian_filter(img3, sigma=7)

img4 = mpimg.imread('adjusted brightfield.jpg')
img4 = gaussian_filter(img4, sigma=7)


def intensity_profile(biolum,bright,row,low=0, high=1388):

    if len(np.shape(biolum)) == 3:
        bio_data = biolum[row, :, 0]
        bright_data = bright[row, :, 0]
        integers = list(range(1, len(bio_data)+1))

    if len(np.shape(biolum)) == 2:
        bio_data = biolum[row, :]
        bright_data = bright[row, :]
        integers = list(range(1, len(bio_data) + 1))

    plt.plot(integers[low:high], bio_data[low:high], label='bioluminescence')
    plt.plot(integers[low:high], bright_data[low:high], label='brightfield')
    plt.xlabel('Column')
    plt.ylabel('Pixel intensity')
    print(row)
    plt.title('Intensity profile at row '+ str(row))
    plt.legend()
    plt.show()

def intensity_profile_interactive(biolum,bright,row,low=0, high=1388):

    if len(np.shape(biolum)) == 3:
        bio_data = biolum[row, :, 0]
        bright_data = bright[row, :, 0]
        integers = list(range(1, len(bio_data)+1))

    if len(np.shape(biolum)) == 2:
        bio_data = biolum[row, :]
        bright_data = bright[row, :]
        integers = list(range(1, len(bio_data) + 1))

    return integers, bio_data, bright_data

 # fig = px.line(integers[low:high], bio_data[low:high])
    # fig.show()
fig, ax = plt.subplots()
plt.subplots_adjust(left = 0.1, bottom = 0.35)

integers, bio_data, bright_data = intensity_profile_interactive(img3, img4, 500)
bio_plot, = plt.plot(integers, bio_data, label='bioluminescence')
bright_plot, = plt.plot(integers, bright_data, label='brightfield')
plt.xlabel('Column')
plt.ylabel('Pixel intensity')
plt.legend()

axSlider = plt.axes([0.1, 0.2, 0.8, 0.05])
row_slider = Slider(axSlider, 'row', valmin=1, valmax=1039, valstep=1)


def val_update(val):
    row = row_slider.val
    bio_plot.set_ydata(intensity_profile_interactive(img3, img4, row)[1])
    bright_plot.set_ydata(intensity_profile_interactive(img3, img4, row)[2])
    plt.draw()

row_slider.on_changed(val_update)
plt.title('Intensity profile',  y=14)
plt.show()

#intensity_profile(img1,img2,800)
#intensity_profile(img3,img4,700)
#intensity_profile_interactive(img3,img4,700)

# axSlider = plt.axes([0.1, 0.2, 0.8, 0.05])
# row_slider = Slider(axSlider, 'row', valmin=1, valmax=1040)