import matplotlib.pyplot as plt
import numpy as np
from skimage.io import imread
from src.processing.marching_squares import marching_squares_contours
from src.processing.constants import BUCKLING_PATH

img1 = imread(BUCKLING_PATH / "200920_biolight_marching_binary.tif")[200]

contours = marching_squares_contours(img1, threshold = 50, max_length = 20)
contours = contours[::300]
fig, ax1 = plt.subplots()
for line in contours:
    line = line[::500]
    ax1.plot(line[:, 1], line[:, 0], linewidth=1, color='red')
    print(len(line))
ax1.set(aspect=1)

plt.show()

print(np.shape(img1))