import numpy as np




def nth_histogram_percentile(image, percentile):
    histogram = np.bincount(np.ravel(image))
    histrogram_cumulative = np.cumsum(histogram)
    histrogram_cumulative = (histrogram_cumulative/histrogram_cumulative[-1])*100
    index_of_percentile = (np.abs(histrogram_cumulative - percentile)).argmin()
    return index_of_percentile