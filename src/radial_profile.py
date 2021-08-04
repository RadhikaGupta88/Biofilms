from include import *
from radius_vs_intensity import txt_to_list

def radial_profile(data, center):
    y, x = np.indices((data.shape))
    r = np.sqrt((x - center[0])**2 + (y - center[1])**2)
    #r = r.astype(np.int)

    tbin = np.bincount(r.ravel(), data.ravel())
    nr = np.bincount(r.ravel())
    radialprofile = tbin / nr
    return radialprofile 



PATH = 'c:/Cambridge/Mechanics_of_biofilm/algorithm for clear images/buckling/'
#img1 = imread(PATH + '200920_normallight_nobg_edges_gaussblur_enhance_inverted.tif')[int(130*1.403726708)]

slice = 160
image = imread(PATH + '200920_biolight_nobg_nooutliers_despeckle_enhance.tif')[slice]


height, width = np.shape(image)
center = (np.array(np.shape(image))/2)
center = center.astype(int)


timestamps_b, radii_b, x_centre_b, y_centre_b = txt_to_list('200920_biolight_fitted_circle_position_data.txt')
x, y = x_centre_b[slice], y_centre_b[slice]


profile = radial_profile(image, (x, y))


#print(profile[10:20])
fig, (ax1, ax2) = plt.subplots(1,2)
#ax2 = plt.gca()
ax2.set_xlim(0.0, width)
ax2.set_ylim(height,0.0)
ax2.imshow(image, cmap = 'Greys')
#ax2.plot(center[1], center[0], 'xg')
ax2.plot(x, y, 'xr')
ax1.plot(profile)
plt.show()