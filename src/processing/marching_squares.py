
import imageio
import matplotlib.pyplot as plt
import numpy as np
import tifffile
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from PIL import Image
from skimage import measure, color
from skimage.io import imread
from tifffile import imwrite

#img1 = imread('c:/Cambridge/Mechanics of biofilm/algorithm for clear images/200920_biolight_marching_edges.tif')[150]
#img1 = imread('c:/Cambridge/Mechanics of biofilm/algorithm for clear images/200920_biolight_marching_binary.tif')
#img1 = imread('c:/Cambridge/Mechanics_of_biofilm/algorithm for clear images/buckling/200920_normallight_bw_imagej.tif')[int(130*1.403726708)]
img1 = imread('c:/Cambridge/Mechanics_of_biofilm/algorithm for clear images/buckling/200920_normallight_nobg_edges_gaussblur_enhance_inverted.tif')[int(130*1.403726708)]
#img1 = imread('c:/Cambridge/Mechanics_of_biofilm/algorithm for clear images/buckling/200920_biolight_nobg_nooutliers_despeckle_enhance.tif')[130]
img_og = imread('c:/Cambridge/Mechanics_of_biofilm/algorithm for clear images/buckling/200920_biolight_nobg_nooutliers_despeckle_enhance.tif')[130]
#img_og = imread('c:/Cambridge/Mechanics of biofilm/algorithm for clear images/200920_normallight_bw_imagej.tif')[200]


def marching_squares_contours(image, threshold = 50, max_length = 20):

    # Find contours at a constant value
    contours = measure.find_contours(image, threshold)

    contours_selective = []
    for contour in contours:
        length = len(contour)
        if length <= max_length:
            pass
        else:
            contours_selective.append(contour)

    return contours_selective


def plot_contours(contours, original_image):
    fig, ax1 = plt.subplots()
    ax1.imshow(original_image, cmap='Greens')
    for line in contours:
        ax1.plot(line[:, 1], line[:, 0], linewidth=1, color='r')
     #ax1.invert_yaxis()
    ax1.set(aspect=1)
    fig.canvas.draw()

    #width, height = fig.get_size_inches() * fig.get_dpi()
    #mplimage = np.fromstring(fig.canvas.tostring_rgb(), dtype='uint8').reshape(height, width, 3)

    data = np.frombuffer(fig.canvas.tostring_rgb(), dtype=np.uint8)
    w, h = fig.canvas.get_width_height()
    data = data.reshape((h, w, 3))
    gray_image = color.rgb2gray(data)


    #fig = np.array(fig)
    #plt.savefig('marching squares stack/image_from_contours_'+str(slice_number)+'.tif', bbox_inches='tight', pad_inches=0)
    #print(type(fig))
    #plt.show()
    #print(type(gray_image))
    plt.show()
    return gray_image


# fig, ax1 = plt.subplots()
# ax1.imshow(img_og, cmap=plt.cm.gray)
# #ax2.imshow(img1, cmap=plt.cm.gray)

def full_stack_contours(stack_name, original_image_stack):
    images = []
    stack = imread(stack_name)
    stack = stack[::100]
    og_images = imread(original_image_stack)
    index = 0
    for image in stack:
        contours = marching_squares_contours(image, 50, 20)
        fig = plot_contours(contours, og_images[index], index+1)
        images.append(fig)
        index += 100
    #im = Image.fromarray(images)
    images = np.dstack(images)
    #print(images[0])
    #tifffile.imsave('full_stack.tiff', images)
    #imageio.mimwrite('full_stack.tiff', images)
    #io.imsave("full stack.png", img_as_uint(images))
    #plt.imsave('full_stack.jpeg', images)
    return images

contours = marching_squares_contours(img1, 16, 20)
plot_contours(contours, img_og)

#plt.axis('off')
#fig.axes.get_xaxis().set_visible(False)
#fig.axes.get_yaxis().set_visible(False)
#plt.savefig('image_from_contours.png', bbox_inches='tight', pad_inches = 0)

def fft_image(image):
    image = np.fft.fftshift(np.fft.fft2(image))
    image = np.log(abs(image))
    return image


# images = full_stack_contours('c:/Cambridge/Mechanics of biofilm/algorithm for clear images/200920_biolight_marching_binary.tif',
#                     'c:/Cambridge/Mechanics of biofilm/algorithm for clear images/200920_biolight_nobg_nooutliers_despeckle_enhance.tif')
#
# rows, columns, slices = np.shape(images)
# images = np.reshape(images, (slices, rows, columns))
#
# #tifffile.imsave('test.tif', images)
# abs = tifffile.imwrite('test.tif', images)
# print(abs)
#
# imgtiff = imread('test.tif')
# print(np.shape(images))
# print(np.shape(imgtiff))
# # print(img)
# # plt.imshow(img)
# # plt.show()
#
# img = imread('c:/Cambridge/Mechanics of biofilm/algorithm for clear images/200920_biolight_marching_binary.tif')
# print(np.shape(img))