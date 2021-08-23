import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Button, Slider
from scipy.ndimage.filters import gaussian_filter
from skimage.io import imread


# img1 = imread('test_biolum.jpg')
# img2 = imread('test_bright.jpg')

#img3 = imread('adjusted biolum.jpg')
#img3 = gaussian_filter(img3, sigma=3)

#img4 = imread('adjusted brightfield.jpg')
#img4 = gaussian_filter(img4, sigma=3)

img3 = imread('c:/Cambridge/Mechanics_of_biofilm/algorithm for clear images/buckling/biolight_gb.tif')[200]
img4 = imread('c:/Cambridge/Mechanics_of_biofilm/algorithm for clear images/buckling/normallight_edge_gb.tif')[200]


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
plt.subplots_adjust(left = 0.1, bottom = 0.35)

integers, bio_data, bright_data = intensity_profile_interactive(img3, img4, 0)

# dx=1
# bright_data = np.diff(bright_data)/dx
# bright_data= np.append(bright_data,[0])


bio_plot, = plt.plot(integers, bio_data, label='bioluminescence')
#bright_plot, = plt.plot(integers, bright_data, label='brightfield')
plt.xlabel('Column')
plt.ylabel('Pixel intensity')
plt.legend()

axSlider = plt.axes([0.1, 0.2, 0.8, 0.05])
row_slider = Slider(axSlider, 'row', valmin=1, valmax=1039, valstep=1)


def val_update(val):
    row = row_slider.val
    bio_plot.set_ydata(intensity_profile_interactive(img3, img4, row)[1])
    #bright_plot.set_ydata(intensity_profile_interactive(img3, img4, row)[2])
    plt.draw()

row_slider.on_changed(val_update)
plt.title('Intensity profile',  y=14)
plt.show()

#intensity_profile(img1,img2,800)
#intensity_profile(img3,img4,700)
intensity_profile_interactive(img3,img4,700)

# axSlider = plt.axes([0.1, 0.2, 0.8, 0.05])
# row_slider = Slider(axSlider, 'row', valmin=1, valmax=1040)
