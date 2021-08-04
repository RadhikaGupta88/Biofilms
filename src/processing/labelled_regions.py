
import random

import matplotlib.pyplot as plt
import numpy as np
from include import *
from radius_vs_intensity import txt_to_list
from skimage import measure

#r = imread('c:/Cambridge/Mechanics_of_biofilm/algorithm for clear images/200920_biolight_marching_binary.tif')
#r = imread('c:/Cambridge/Mechanics_of_biofilm/algorithm for clear images/buckling/200920_normallight_nobg_edges_gaussblur_enhance_inverted.tif')
r = imread('c:/Cambridge/Mechanics_of_biofilm/algorithm for clear images/buckling/200920_biolight_nobg_nooutliers_despeckle_enhance.tif')
#r = imread('c:/Cambridge/Mechanics_of_biofilm/algorithm for clear images/200920_normallight_nobg_inverted.tif')

# Coordinates of point of interest
#pt = [(49,75)]


def label_regions(image, threshold_low, threshold_high = 255, plot= False):
    blobs = image
    blobs = blobs > threshold_low
    #blobs[blobs <= threshold_low] = 0
    #blobs[blobs >= threshold_high] = 0
    blobs_labels = measure.label(blobs, background = 0)

    if plot==True:
        plt.figure()
        plt.imshow(blobs_labels, cmap='rainbow')
        plt.show()

    return blobs_labels


def create_contours(labelled_image, lower_contour_bound = 50, upper_contour_bound = 10000000000):
    all_props = measure.regionprops(labelled_image)
    coord_list = []
    for prop in all_props:
        coords = prop.coords
        if lower_contour_bound <= len(coords) <= upper_contour_bound:
            coord_list.append(coords)
    return coord_list

def characterise_regions(image, labelled_image, lower_contour_bound = 50, upper_contour_bound = 1000000, plot = False):
    #props = measure.regionprops(labelled_image, intensity_image=image)
    props = measure.regionprops(labelled_image)

    #print('image shape passed: ', np.shape(image))
    total_area = 0
    area_list = []
    for prop in props:
        coords = prop.coords
        #weighted_centroid = prop.weighted_centroid
        #minr, minc, maxr, maxc = prop.bbox
        if lower_contour_bound <= len(coords) <= upper_contour_bound:
            area = prop.area
            total_area += area
            area_list.append(area)
            if plot == True:
                #plt.plot(coords[:, 1], coords[:, 0], 'o', ms=0.05, color=np.random.rand(3,))
                plt.plot(coords[:, 1], coords[:, 0], 'go', ms=0.1)
            # coords = coords[::50]
            #plt.plot(coords[:, 1], coords[:, 0], 'o', ms=0.1)
            # plt.plot(weighted_centroid, 'r')
            #bx = (minc, maxc, maxc, minc, minc)
            #by = (minr, minr, maxr, maxr, minr)
            #plt.plot(bx, by, '-b', linewidth=1.0)
        # if np.sum(np.all(coords[:,[1,0]] == pt[0], axis=1)):
        #    plt.plot(coords[:,1],coords[:,0],'r.')
        #   print(prop.area)
    average_area = sum(area_list) / len(area_list)
    if plot == True:
        plt.imshow(image, cmap='Reds')
        plt.show()
    return total_area, average_area


#slice = imread('c:/Cambridge/Mechanics_of_biofilm/algorithm for clear images/asymmetric/normallight_edges.tif')[160]
#slice = imread('c:/Cambridge/Mechanics_of_biofilm/algorithm for clear images/Paraview images/colour_by_z_coord_inverted_edges.png')
#img = label_regions(slice, 100, 200, plot=True)
#slice = imread('c:/Cambridge/Mechanics_of_biofilm/algorithm for clear images/asymmetric/normallight_edges.tif')[160]
#total_area, average_area = characterise_regions(slice, img, 0, 10000000000, plot=True)
#r = r[::50]


lit_areas = []
average_areas = []
for slice in r:
    img = label_regions(slice, 20)
    #characterise_regions(slice, img, 10)
    lit_area, average_area = characterise_regions(slice, img)
    lit_areas.append(lit_area)
    average_areas.append(average_area)


timestamps_b, radii_b, x_centre_b, y_centre_b = txt_to_list('200920_biolight_fitted_circle_position_data.txt')

#circular_areas = math.pi*np.array(radii_b)**2
normalized_areas = np.array(lit_areas)/(math.pi * np.array(radii_b) ** 2)
frames = np.linspace(1,322,322)
frames = frames*(1/6)
#print(frames)

#plt.plot(timestamps_b, average_areas)
plt.plot(frames, normalized_areas, color='g')
plt.xlabel('Hours')
plt.ylabel('Fraction of biofilm luminescing')
plt.show()



#--------------------------------------------------------------------------
#------------------------------------------------------------------------internet code
# # Apply thresholding to the surface
# threshold = 0.8
# blobs = r > threshold
#
# # Make a labelled image based on the thresholding regions
# blobs_labels = measure.label(blobs, background = 0)
#
# # Show the thresholded regions
# plt.figure()
# plt.imshow(blobs_labels, cmap='rainbow')
# plt.show()
#
# # Apply regionprops to charactersie each of the regions
# props = measure.regionprops(blobs_labels, intensity_image = r)

# Loop through each region in regionprops, identify if the point of interest is
# in that region. If so, plot the region and print it's area.
# plt.figure()
# plt.imshow(r, cmap='Greys')
# #plt.plot(pt[0][0], pt[0][1],'rx')
# for prop in props:
#     coords = prop.coords
#     weighted_centroid = prop.weighted_centroid
#     minr, minc, maxr, maxc = prop.bbox
#     area = prop.area
#     if 100<=len(coords)<=1000000:
#         #coords = coords[::50]
#         plt.plot(coords[:, 1], coords[:, 0], 'o', ms=0.1)
#         #plt.plot(weighted_centroid, 'r')
#         bx = (minc, maxc, maxc, minc, minc)
#         by = (minr, minr, maxr, maxr, minr)
#         plt.plot(bx, by, '-b', linewidth=1.0)
#         print(area)
#     #print(prop.area)
#     #if np.sum(np.all(coords[:,[1,0]] == pt[0], axis=1)):
#     #    plt.plot(coords[:,1],coords[:,0],'r.')
#      #   print(prop.area)
#
# plt.show()