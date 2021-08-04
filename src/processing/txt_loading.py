import numpy as np
from src.constants import MECHANICS_OF_BIOFILM_PATH

def txt_to_list(name):

    with open(MECHANICS_OF_BIOFILM_PATH / 'George algorithm/Data_Storage/200920' /  str(name)) as f:
        contents = [line.split(',') for line in f]

    rows = len(contents)
    contents = np.array(contents).reshape(rows, 4)
    timestamps = list(np.float_(contents[1:,0]))
    radii = list(np.float_(contents[1:,1]))
    x_centre = list(np.float_(contents[1:,2]))
    y_centre = list(np.float_(contents[1:,3]))

    return timestamps, radii, x_centre, y_centre