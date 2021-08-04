import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
import skimage
from include import *
from skimage import io

#img1 = io.imread('c:/Cambridge/Mechanics of biofilm/algorithm for clear images/200920_biolight_nobg_nooutliers_despeckle_enhance.tif')[200]
#img1_flat = np.array(img1).flatten().tolist()
#img2= io.imread('c:/Cambridge/Mechanics of biofilm/algorithm for clear images/200920_normallight_nobg_edges_gaussblur_enhance.tif')[200]
#img2_flat = np.array(img2).flatten().tolist()
img1 = mpimg.imread('adjusted biolum.jpg')
# img1 = mpimg.imread('test_biolum.jpg')
# img1 = img1[:,60,0]
img1_flat = img1[300]
img1_flat = np.array(img1).flatten().tolist()

img2 = mpimg.imread('adjusted brightfield.jpg')
#img2 = filters.laplace(img2, ksize=3, mask=None)
img2 = filters.difference_of_gaussians(img2, 2, 6, mode='nearest', cval=0)
img2 = skimage.exposure.match_histograms(img2, img1)
# img2 = mpimg.imread('test_bright.jpg')
# img2 = img2[:,60,0]
img2_flat = img2[300]
img2_flat = np.array(img2).flatten().tolist()


#m, b = np.polyfit(img1_flat, img2_flat, 1)
#print(m,b)
#fit = m*img1 + b
#fit_flat = np.array(fit).flatten().tolist()
#print(img1)
#print(img2)
fig, (ax1, ax2, ax3) = plt.subplots(1,3)
ax1.plot(img1_flat, img2_flat, 'o', ms=1)
ax2.imshow(img1)
ax3.imshow(img2)
#plt.plot(img1_flat, fit_flat)
#plt.imshow(img2)
#plt.show()
plt.show()


