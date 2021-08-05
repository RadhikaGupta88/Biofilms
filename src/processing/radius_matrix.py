import numpy as np
import matplotlib.pyplot as plt
from skimage import data
from skimage.io import imread

PATH = 'c:/Cambridge/Mechanics_of_biofilm/algorithm for clear images/buckling/'
#img1 = imread(PATH + '200920_normallight_nobg_edges_gaussblur_enhance_inverted.tif')[int(130*1.403726708)]

image = imread(PATH + '200920_biolight_nobg_nooutliers_despeckle_enhance.tif')[130]


# create array of radii
x,y = np.meshgrid(np.arange(image.shape[1]),np.arange(image.shape[0]))
R = np.sqrt(x**2+y**2)

# calculate the mean
f = lambda r : image[(R >= r-.5) & (R < r+.5)].mean()
r  = np.linspace(1,302,num=302)
mean = np.vectorize(f)(r)

circle = image[(R >= 40-.5) & (R < 40+.5)]

# plot it
fig,ax= plt.subplots()
ax.imshow(image)

ax.plot(circle)
plt.show()