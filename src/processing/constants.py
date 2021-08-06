"""All project wide constants are saved in this module."""
# Place all your constants here
import os
import pathlib

# Note: constants should be UPPER_CASE
constants_path = pathlib.Path(os.path.realpath(__file__))
SRC_PATH = pathlib.Path(os.path.dirname(constants_path))
PROJECT_PATH = pathlib.Path(os.path.dirname(SRC_PATH))

DATA_PATH = PROJECT_PATH / "Data"

if os.name == "nt":  # if running windows
    MECHANICS_OF_BIOFILM_PATH = pathlib.Path('c:/Cambridge/Mechanics_of_biofilm')
elif os.name == "posix":  # if running linux
    MECHANICS_OF_BIOFILM_PATH = pathlib.Path("/mnt/c/Cambridge/Mechanics_of_biofilm")

BUCKLING_PATH = MECHANICS_OF_BIOFILM_PATH / "algorithm for clear images" / "buckling"
EDGE_TRACKING_PATH = MECHANICS_OF_BIOFILM_PATH  / "George algorithm" / "Data_Storage" / "200920" 
NEW_MOVIE_PATH = MECHANICS_OF_BIOFILM_PATH  / "algorithm for clear images" / "new_movies" 