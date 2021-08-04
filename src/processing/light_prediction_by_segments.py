
from include import *
from labelled_regions import (characterise_regions, create_contours,
                              label_regions)


def plot_all_segments(stack, slice_no):

    image1 = stack[slice_no]
    image2 = stack[slice_no]
    image3 = stack[slice_no]
    #print(np.min(image), np.max(image))

    print('creating labelled images...')
    img_1 = label_regions(image1, 50)
    #print(np.min(img_1), np.max(img_1))
    img_2 = label_regions(image2, 30)
    #print(np.min(img_2), np.max(img_2))
    img_3 = label_regions(image3, 60)
    #print(np.min(img_3), np.max(img_3))

    print('creating contours...')
    coords_1 = create_contours(img_1, 0)
    coords_2 = create_contours(img_2, 0)
    coords_3 = create_contours(img_3, 0)
    print(len(coords_1), len(coords_2), len(coords_3))

    print('plotting blue...')
    #for coords in coords_1:
     #   plt.plot(coords[:, 1], coords[:, 0], 'o', ms=0.5, color='coral')

    print('plotting green...')
    for coords in coords_2:
        plt.plot(coords[:, 1], coords[:, 0], 'o', ms=0.5, color='red')

    print('plotting red...')
    for coords in coords_3:
        plt.plot(coords[:, 1], coords[:, 0], 'o', ms=0.5, color='darkred')

    plt.gca().invert_yaxis()
    plt.gca().set_aspect('equal')
    plt.show()

    print('Finished')



plot_all_segments(imread('c:/Cambridge/Mechanics_of_biofilm/algorithm for clear images/asymmetric/normallight_edges.tif'), 160)