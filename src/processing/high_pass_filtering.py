from include import *
from scipy import ndimage
from skimage import filters

#stack_b = imread('c:/Cambridge/Mechanics of biofilm/original videos/200920_biolight_orginal.tif')
#stack_n = imread('c:/Cambridge/Mechanics of biofilm/original videos/200920_normallight_orginal.tif')

stack_b = imread('c:/Cambridge/Mechanics of biofilm/algorithm for clear images/200920_biolight_nobg_nooutliers_despeckle.tif')
stack_n = imread('c:/Cambridge/Mechanics of biofilm/algorithm for clear images/200920_normallight_nobg.tif')

slice = 300
img_b = stack_b[slice]
img_b = gaussian_filter(img_b, sigma=1)
#img_n = stack_n[slice]

img_n = stack_n[slice]

#img_fft_b = fft_image(img_b)
#img_fft_n = fft_image(img_n)

kernel = np.array([[-1, -1, -1, -1, -1],
                   [-1,  1,  2,  1, -1],
                   [-1,  2,  4,  2, -1],
                   [-1,  1,  2,  1, -1],
                   [-1, -1, -1, -1, -1]])


# kernel = np.array([[-1, -1, -1],
#                    [-1,  8, -1],
#                    [-1, -1, -1]])

fig, (ax1, ax2) = plt.subplots(1,2)

highpass_5x5 = ndimage.convolve(img_n, kernel)
#gauss = gaussian_filter(highpass_5x5, sigma=8)
ax1.imshow(highpass_5x5, cmap='gray')
#
# kernel = np.array([[0, 1, 0],
#                     [1,  1, 1],
#                     [0, 1, 0]])
#image = ndimage.convolve(highpass_5x5, kernel)
#ax2.imshow(image, cmap='gray')
#plt.show()


band_pass = filters.difference_of_gaussians(img_n, 0, 8, mode='nearest', cval=0)
laplace = filters.laplace(img_n, ksize=5, mask=None)
ax2.imshow(band_pass, cmap='gray')
plt.show()
#
# rows, cols = img_b.shape
# crow, ccol = int(rows / 2), int(cols / 2)  # center
#
# # Circular HPF mask, center circle is 0, remaining all ones
#
# mask = np.ones((rows, cols, 2), np.uint8)
# r = 80
# center = [crow, ccol]
# x, y = np.ogrid[:rows, :cols]
# mask_area = (x - center[0]) ** 2 + (y - center[1]) ** 2 <= r*r
# mask[mask_area] = 1
#
# # apply mask and inverse DFT
# fshift = dft_shift * mask
#
# fshift_mask_mag = 2000 * np.log(cv2.magnitude(fshift[:, :, 0], fshift[:, :, 1]))
#
# f_ishift = np.fft.ifftshift(fshift)
# img_back = cv2.idft(f_ishift)
# img_back = cv2.magnitude(img_back[:, :, 0], img_back[:, :, 1])
#
# plt.subplot(2, 2, 1), plt.imshow(img, cmap='gray')
# plt.title('Input Image'), plt.xticks([]), plt.yticks([])
# plt.subplot(2, 2, 2), plt.imshow(magnitude_spectrum, cmap='gray')
# plt.title('After FFT'), plt.xticks([]), plt.yticks([])
# plt.subplot(2, 2, 3), plt.imshow(fshift_mask_mag, cmap='gray')
# plt.title('FFT + Mask'), plt.xticks([]), plt.yticks([])
# plt.subplot(2, 2, 4), plt.imshow(img_back, cmap='gray')
# plt.title('After FFT Inverse'), plt.xticks([]), plt.yticks([])
# plt.show()