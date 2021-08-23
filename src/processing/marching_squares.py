import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from skimage import measure, color
from skimage.io import imread
from tifffile import imwrite


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
    fig.set_size_inches(10,10)
    ax1.imshow(original_image, cmap='Greens')
    for line in contours:
        ax1.plot(line[:, 1], line[:, 0], linewidth=1, color='r')
     #ax1.invert_yaxis() #for when not plotting the image as well
    ax1.set(aspect=1)
    fig.canvas.draw()

    data = np.frombuffer(fig.canvas.tostring_rgb(), dtype=np.uint8)
    w, h = fig.canvas.get_width_height()
    data = data.reshape((h, w, 3))
    gray_image = color.rgb2gray(data)


    #fig = np.array(fig)
    #plt.savefig('marching squares stack/image_from_contours_'+str(slice_number)+'.tif', bbox_inches='tight', pad_inches=0)

    plt.show()
    return gray_image



#not yet fully implemented...
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
