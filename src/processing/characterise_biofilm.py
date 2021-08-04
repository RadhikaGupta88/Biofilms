
import matplotlib.pyplot as plt
import math
from skimage.io import imread
from src.labelled_regions import (characterise_regions, create_contours,
                              label_regions)
from src.radius_vs_intensity import txt_to_list

from src.constants import BUCKLING_PATH


def characterise_biofilm_image(stack, slice_no, type = 0):
    #type 0 is brightfield and type 1 is biolum
    
    slice = stack[slice_no]

    if type == 0:
        film = 'Brightfield'
        img = label_regions(slice, 15)
        lit_area, average_area = characterise_regions(slice, img, 20, plot = True)
        timestamps, radii, x_centres, y_centres = txt_to_list('200920_normallight_fitted_circle_position_data.txt')

    if type == 1:
        film = 'Bioluminescence'
        img = label_regions(slice, 50)
        lit_area, average_area = characterise_regions(slice, img, 50, plot = True)
        timestamps, radii, x_centres, y_centres = txt_to_list('200920_biolight_fitted_circle_position_data.txt')
    
    print(f"{film} image, slice {slice_no}/{len(stack)}")

    timestamp = timestamps[slice_no]
    radius = radii[slice_no]
    x_centre = x_centres[slice_no]
    y_centre = y_centres[slice_no]
    coffe_ring_radius = 0

    print(f'Timestamp: {timestamp}')
    print(f'Total lit area: {lit_area}')
    print(f'Fraction of biofilm lit: {lit_area/(math.pi*radius**2)}')
    print(f'Average area of lit region: {average_area}')
    print(f'Biofilm radius: {radius}\n'.format(radius))




def characterise_both_biofilm_images(stack_n, stack_b, slice_no_b):
    #type 0 is brightfield and type 1 is biolum
    STACK_B_TO_N_RATIO = len(stack_b) / len(stack_n)
    slice_no_n = int(slice_no_b * STACK_B_TO_N_RATIO)
    slice_n = stack_n[slice_no_n]
    slice_b = stack_b[slice_no_b]

    img_n = label_regions(slice_n, 15)
    img_b = label_regions(slice_b, 55)

    coords_n = create_contours(img_n, 0)
    coords_b = create_contours(img_b, 50)

    for coords in coords_n:
        plt.plot(coords[:, 1], coords[:, 0], 'ro', ms=0.1)

    for coords in coords_b:
        plt.plot(coords[:, 1], coords[:, 0], 'go', ms=0.05)

    plt.gca().invert_yaxis()
    plt.gca().set_aspect('equal')
    plt.show()



slice = 130

r = imread(BUCKLING_PATH / "200920_normallight_nobg_edges_gaussblur_enhance_inverted.tif")
s = imread(BUCKLING_PATH / "200920_biolight_nobg_nooutliers_despeckle_enhance.tif"s)
#characterise_biofilm_image(r, int(slice* 1.403726708), 0)
#characterise_biofilm_image(s, slice, 1)

characterise_both_biofilm_images(r, s, slice)

#for i in range(0,2):
 #   characterise_biofilm_image(r, i, 0)
#def characterise_biofilm_stack()

