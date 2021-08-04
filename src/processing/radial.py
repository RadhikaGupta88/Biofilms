import numpy as np

def radial_select(image, center, target_radius, tolerance=1.):
    y, x = np.indices((image.shape))
    pixel_radius = np.sqrt((x - center[0])**2 
                           + (y - center[1])**2
                          )  # calculate radii of all pixels from center (shape is same as data)
    
    pixel_in_disk = np.logical_and(target_radius - tolerance <= pixel_radius, 
                               pixel_radius <= target_radius + tolerance)
    
    disk_y_coords, disk_x_coords = np.where(pixel_in_disk)
    disk_values = image[disk_y_coords, disk_x_coords]
    
    return disk_y_coords, disk_x_coords, disk_values


def order_coords(disk_y_coords, disk_x_coords, disk_values, center):
    disk_phi_coords = (np.arctan2(disk_y_coords - center[1], disk_x_coords - center[0]))
    stack = np.vstack([disk_x_coords, disk_y_coords, disk_values, disk_phi_coords])
    sorted_stack = stack[:,stack[3,:].argsort()]
    return sorted_stack

