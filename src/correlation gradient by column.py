import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


#img1 = mpimg.imread('adjusted biolum.jpg')
img1 = mpimg.imread('test_biolum.jpg')
rows1, columns1, pixels1 = np.shape(img1)
#img2 = mpimg.imread('adjusted brightfield.jpg')
img2 = mpimg.imread('test_bright.jpg')
rows2, columns2, pixels2 = np.shape(img2)

#print(columns1, columns2)

row_values1 = []
row_values2 = []
m=[]
b=[]

for column in range(columns1):
    row_values1 = img1[:,column,0]
    row_values2 = img2[:,column,0]
    m.append(np.polyfit(row_values1, row_values2, 1)[0])

#print(len(m))

integers = list(range(1, columns1+1))
integers = integers[60:1300]
m = m[60:1300]


plt.plot(integers, m, 'o', ms=1)
# plt.plot(img1_flat, fit_flat)
plt.show()