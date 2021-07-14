import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


#img1 = mpimg.imread('adjusted biolum.jpg')
img1 = mpimg.imread('test_biolum.jpg')
img1 = img1[:,60,0]
#img1 = img1[150:200]
img1_flat = np.array(img1).flatten().tolist()

# for i in range(len(img1)-1):
#     if img1[i] > 200:
#         img1[i] = 254
#     if img1[i] < 50:
#         img1[i] = 0

#img2 = mpimg.imread('adjusted brightfield.jpg')
img2 = mpimg.imread('test_bright.jpg')
img2 = img2[:,60,0]
#img2 = img2[150:200]
img2_flat = np.array(img2).flatten().tolist()
# for i in range(len(img2)-1):
#     if img2[i] > 200:
#         img2[i] = 254
#     if img2[i] < 50:
#         img2[i] = 0


m, b = np.polyfit(img1_flat, img2_flat, 1)
print(m,b)
fit = m*img1 + b
fit_flat = np.array(fit).flatten().tolist()
#print(img1)
#print(img2)
plt.plot(img1_flat, img2_flat, 'o', ms=1)
plt.plot(img1_flat, fit_flat)
#plt.imshow(img2)
#plt.show()
plt.show()


