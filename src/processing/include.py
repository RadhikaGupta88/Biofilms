import math

import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from matplotlib.widgets import Button, Slider

import numpy as np

import skimage.color as color
import skimage.data as data
import skimage.draw as draw
import skimage.filters as filters
import skimage.segmentation as seg


from scipy import ndimage
from scipy.ndimage.filters import gaussian_filter

from skimage import color, exposure, filters, transform
from skimage.color import rgb2gray, rgb2hsv, rgb2yuv
from skimage.exposure import equalize_hist
from skimage.io import imread, imsave, imshow
