from include import *
import scipy

PATH = 'c:/Cambridge/Mechanics_of_biofilm/algorithm for clear images/buckling/'
#img1 = imread(PATH + '200920_normallight_nobg_edges_gaussblur_enhance_inverted.tif')[int(130*1.403726708)]

img1 = imread(PATH + '200920_biolight_nobg_nooutliers_despeckle_enhance.tif')[130]
img2 = imread(PATH + '200920_biolight_nobg_nooutliers_despeckle_enhance.tif')[140]

img3  = scipy.ndimage.rotate(img1, 90)
#data = scipy.signal.correlate2d(img1, img2)
#plt.plot(data)
#plt.acorr(img1)
fig, (ax1, ax2) = plt.subplots(1,2)
#ax1.imshow(img1)
#ax2.imshow(scipy.ndimage.rotate(img1, 45))

#plt.show()

#data = scipy.signal.correlate2d(img3, img3)

print(np.shape(img1))
print(np.shape(img3))