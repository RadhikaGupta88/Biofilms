import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
import pandas
import plotly.express as px
from matplotlib.widgets import Button, Slider
from scipy.ndimage.filters import gaussian_filter

img1 = mpimg.imread('test_biolum.jpg')
img2 = mpimg.imread('test_bright.jpg')

img3 = mpimg.imread('adjusted biolum.jpg')
img3 = gaussian_filter(img3, sigma=3)
rows3, columns3 = np.shape(img3)

img4 = mpimg.imread('adjusted brightfield.jpg')
img4 = gaussian_filter(img4, sigma=3)


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


fig, (ax1, ax2) = plt.subplots(1,2)
plt.subplots_adjust(left = 0.1, bottom = 0.35)

#subplot 1
integers, bio_data, bright_data = intensity_profile_interactive(img3, img4, 500)
bio_plot, = ax1.plot(integers, bio_data, label='bioluminescence')
bright_plot, = ax1.plot(integers, bright_data, label='brightfield')
ax1.set_xlabel('Column')
ax1.set_ylabel('Pixel intensity')
ax1.set_title('Intensity profile')
# ax1.xlabel('Column')
# ax1.ylabel('Pixel intensity')
plt.legend()

axSlider = plt.axes([0.1, 0.2, 0.8, 0.05])
row_slider = Slider(axSlider, 'row', valmin=1, valmax=1039, valstep=1)

#subplot 2
ax2.imshow(img4)
line, = ax2.plot(np.zeros(columns3), color='r', linestyle='-')
ax2.set_title('Brightfield image')

def val_update(val):
    row = row_slider.val
    bio_plot.set_ydata(intensity_profile_interactive(img3, img4, row)[1])
    bright_plot.set_ydata(intensity_profile_interactive(img3, img4, row)[2])
    line.set_ydata(row)
    plt.draw()

row_slider.on_changed(val_update)

#plt.title('Intensity profile',  y=14)
plt.show()

#intensity_profile(img1,img2,800)
#intensity_profile(img3,img4,700)
#intensity_profile_interactive(img3,img4,700)

# axSlider = plt.axes([0.1, 0.2, 0.8, 0.05])
# row_slider = Slider(axSlider, 'row', valmin=1, valmax=1040)