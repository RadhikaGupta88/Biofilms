import matplotlib.pyplot as plt
import numpy as np
import skimage.segmentation as seg

from skimage.io import imread


img1 = imread('c:/Cambridge/Mechanics of biofilm/algorithm for clear images/200920_biolight_nobg_nooutliers_despeckle_enhance.tif')[150]
img2 = imread('c:/Cambridge/Mechanics of biofilm/algorithm for clear images/200920_biolight_nobg_nooutliers_despeckle_enhance.tif')[160]


rows, columns = np.shape(img1)

def image_show(image, nrows=1, ncols=1, cmap='gray'):
    fig, ax = plt.subplots(nrows=nrows, ncols=ncols, figsize=(14, 14))
    ax.imshow(image, cmap='gray')
    ax.axis('off')
    return fig, ax

def circle_points(resolution, center, radius):
    """
    Generate points which define a circle on an image.Centre refers to the centre of the circle
    """
    radians = np.linspace(0, 2 * np.pi, resolution)
    c = center[1] + radius * np.cos(radians)  # polar co-ordinates
    r = center[0] + radius * np.sin(radians)

    return np.array([c, r]).T


# Exclude last point because a closed path should not have duplicate points
points = circle_points(200, [(rows/2) -1, (columns/2)-1], 450)[:-1]

#fig, ax = image_show(img1)
#ax.plot(points[:, 0], points[:, 1], '--r', lw=3)
#plt.show()

snake = seg.active_contour(img1, points)
fig, ax = image_show(img1)
ax.plot(points[:, 0], points[:, 1], '--r', lw=3)
ax.plot(snake[:, 0], snake[:, 1], '-b', lw=3)
plt.show()