from skimage.io import imread
import numpy as np
import matplotlib.pyplot as plt

#
# stack_b = imread('c:/Cambridge/Mechanics of biofilm/algorithm for clear images/biolight_gb.tif')
# stack_n = imread('c:/Cambridge/Mechanics of biofilm/algorithm for clear images/normallight_edge_gb.tif')

stack_b = imread('c:/Cambridge/Mechanics of biofilm/original videos/200920_biolight_orginal.tif')
stack_n = imread('c:/Cambridge/Mechanics of biofilm/original videos/200920_normallight_orginal.tif')

def slice_from_stack(stack, slice):
    image = stack[slice]
    return image

def fft_image(image):
    image = np.fft.fftshift(np.fft.fft2(image))
    image = np.log(abs(image))
    return image


img_b = slice_from_stack(stack_b, 10)
img_n = slice_from_stack(stack_n, 10)
img_fft_b = fft_image(img_b)
img_fft_n = fft_image(img_n)

# set up figure
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(10, 10))
plt.subplots_adjust(left = 0.1, bottom = 0.35)

# create slider
axSlider = plt.axes([0.1, 0.2, 0.8, 0.05])
slice_slider = Slider(axSlider, 'stack slice', valmin=1, valmax=322, valstep=1)

plot_b = ax1.imshow(img_b)
plot_n = ax2.imshow(img_n)

plot_fft_b = ax3.imshow(img_fft_b)
plot_fft_n = ax4.imshow(img_fft_n)


def val_update(val):
    slice = slice_slider.val - 1

    img_b = slice_from_stack(stack_b, slice)
    img_n = slice_from_stack(stack_n, slice)

    img_fft_b = fft_image(img_b)
    img_fft_n = fft_image(img_n)

    plot_b.set_data(img_b)
    plot_n.set_data(img_n)

    plot_fft_b.set_data(img_fft_b)
    plot_fft_n.set_data(img_fft_n)

    plt.draw()
    #plt.show()


slice_slider.on_changed(val_update)

plt.show()