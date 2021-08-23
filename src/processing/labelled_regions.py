
import matplotlib.pyplot as plt
from skimage import measure


def label_regions(image, threshold_low, threshold_high = 255, plot= False):
    """
    Creates as labelled image from an unlabelled one
    """
    blobs = image
    blobs = blobs > threshold_low #clip array at the low threshold
    #blobs[blobs <= threshold_low] = 0
    #blobs[blobs >= threshold_high] = 0
    blobs_labels = measure.label(blobs, background = 0)

    if plot==True:
        plt.figure()
        plt.imshow(blobs_labels, cmap='rainbow')
        plt.show()

    return blobs_labels



def create_contours(labelled_image, lower_contour_bound = 50, upper_contour_bound = 10000000000):

    """
    creates regions from labelled image and returns coordinate lists for region edges
    """
    all_props = measure.regionprops(labelled_image)
    coord_list = []
    for prop in all_props:
        coords = prop.coords
        if lower_contour_bound <= len(coords) <= upper_contour_bound:
            coord_list.append(coords)
    return coord_list



def characterise_regions(image, labelled_image, lower_contour_bound = 50, upper_contour_bound = 1000000, plot = False):

    """
    Takes a labelled image and returns the total lit up area and the average area of a lit up region.
    Plots regions on top of original image if desired
    """
    #props = measure.regionprops(labelled_image, intensity_image=image)
    props = measure.regionprops(labelled_image)

    #print('image shape passed: ', np.shape(image))

    total_area = 0
    area_list = []
    plt.figure(figsize=(10, 10), dpi=80)
    for prop in props:
        coords = prop.coords

        #uncomment to plot bounding box for each region
        #minr, minc, maxr, maxc = prop.bbox

        if lower_contour_bound <= len(coords) <= upper_contour_bound:
            area = prop.area
            total_area += area
            area_list.append(area)
            if plot == True:

                #uncomment to plot each region in a different colour
                #plt.plot(coords[:, 1], coords[:, 0], 'o', ms=0.05, color=np.random.rand(3,))

                plt.plot(coords[:, 1], coords[:, 0], 'go', ms=0.1)

                #uncomment to plot bounding box for each region
                #bx = (minc, maxc, maxc, minc, minc)
                #by = (minr, minr, maxr, maxr, minr)
                #plt.plot(bx, by, '-b', linewidth=1.0)

    average_area = sum(area_list) / len(area_list)
    if plot == True:
        plt.imshow(image, cmap='Reds')
        plt.show()
    return total_area, average_area
