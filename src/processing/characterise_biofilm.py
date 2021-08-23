
import matplotlib.pyplot as plt
import math
<<<<<<< HEAD
from skimage.io import imread
from src.processing.labelled_regions import (characterise_regions, create_contours, label_regions)
from src.processing.txt_loading import txt_to_list
from src.processing.constants import BUCKLING_PATH
=======
from src.processing.labelled_regions import characterise_regions, create_contours, label_regions
from src.processing.radius_vs_intensity import txt_to_list
>>>>>>> main

def characterise_biofilm_image(stack, slice_no, type = 0, label_threshold = 50):

    """
    Takes a tif stack, either biolight or brightfield, and given a particular slice number,
    returns properties such as the average lit area and average area of lit region, etc.

    Note: biofilm areas are taken from edge tracking algorithm outputs performed on the high density
    buckling vidoes. These will not be valid for other movies.

    Set slice_no to None, if you want to input a single image from a stack.
    """

    #type 0 is brightfield and type 1 is biolum
    if slice_no == None:
        slice = stack
    else:
        slice = stack[slice_no]

    if type == 0:
        film = 'Brightfield'
        img = label_regions(slice, label_threshold)
        lit_area, average_area = characterise_regions(slice, img, 20, plot = True)
        timestamps, radii, x_centres, y_centres = txt_to_list('200920_normallight_fitted_circle_position_data.txt')

    if type == 1:
        film = 'Bioluminescence'
        img = label_regions(slice, label_threshold)
        lit_area, average_area = characterise_regions(slice, img, 50, plot = True)
        timestamps, radii, x_centres, y_centres = txt_to_list('200920_biolight_fitted_circle_position_data.txt')

    print(f"{film} image, slice {slice_no}/{len(stack)}")

    timestamp = timestamps[slice_no]
    radius = radii[slice_no]
    x_centre = x_centres[slice_no]
    y_centre = y_centres[slice_no]
    coffee_ring_radius = radii[0]

    coffee_ring_radius_fraction = coffee_ring_radius/radius

    print(f'Timestamp: {timestamp}')
    print(f'Total lit area: {lit_area}')
    print(f'Fraction of biofilm lit: {lit_area/(math.pi*radius**2)}')
    print(f'Average area of lit region: {average_area}')
    print(f'Biofilm radius: {radius}')
    print(f'Coffee ring radius: {coffee_ring_radius_fraction} x biofilm radius\n')




def characterise_both_biofilm_images(stack_n, stack_b, slice_no_b):
    """
    Takes a brightfiled stack and biolight stack and, given a biolight slice number,
    plots the edges for both images and displayes together.
    """
    #type 0 is brightfield and type 1 is biolum
    STACK_B_TO_N_RATIO = len(stack_b) / len(stack_n)
    slice_no_n = int(slice_no_b / STACK_B_TO_N_RATIO)
    slice_n = stack_n[slice_no_n]
    slice_b = stack_b[slice_no_b]

    img_n = label_regions(slice_n, 15)
    img_b = label_regions(slice_b, 55)

    coords_n = create_contours(img_n, 0)
    coords_b = create_contours(img_b, 50)

    plt.figure(figsize=(10, 10), dpi=80)

    for coords in coords_n:
        plt.plot(coords[:, 1], coords[:, 0], 'ro', ms=0.1)

    for coords in coords_b:
        plt.plot(coords[:, 1], coords[:, 0], 'go', ms=0.05)

    plt.gca().invert_yaxis()
    plt.gca().set_aspect('equal')
    plt.show()
