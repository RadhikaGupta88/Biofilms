import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider


def fft_image(image):
    """
    Finds and returns the fourier spectrum of an image
    """
    image = np.fft.fftshift(np.fft.fft2(image))
    image = np.log(abs(image))
    return image


def plot_fourier_spectrum_subplots(stack_b, stack_n):
    """
    Creates an interactive set of 4 subplots, two of which are images from given biolight
    and brightfield stacks, and the other two are their fourier spectrums
    """

    slice_no_b = 10
    STACK_B_TO_N_RATIO = len(stack_b) / len(stack_n)
    slice_no_n = int(slice_no_b / STACK_B_TO_N_RATIO)

    img_b = stack_b[slice_no_b]
    img_n = stack_n[slice_no_n]
    img_fft_b = fft_image(img_b)
    img_fft_n = fft_image(img_n)

    # set up figure
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(10, 10))
    plt.subplots_adjust(left = 0.1, bottom = 0.35)

    # create slider
    axSlider = plt.axes([0.1, 0.2, 0.8, 0.05])
    slice_slider = Slider(axSlider, 'stack slice', valmin=1, valmax=322, valstep=1)

    plot_b = ax1.imshow(img_b, cmap='gray')
    plot_n = ax2.imshow(img_n, cmap='gray')

    plot_fft_b = ax3.imshow(img_fft_b, cmap='gray')
    plot_fft_n = ax4.imshow(img_fft_n, cmap='gray')


    def val_update(val):
        slice = slice_slider.val - 1

        img_b = stack_b[slice]
        img_n = stack_n[int(slice / STACK_B_TO_N_RATIO)]

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