import numpy as np
import matplotlib.pyplot as plt


def autocorrelate_single_value(data, lag):
    """
    Returns the normalized autocorrelation for a list of data given a specific lag
    """
    return np.corrcoef(data, np.concatenate([data[lag:], data[:lag]]))[0,1]


def autocorrelate_radial_ring(ring_data, plot = False):
    """
    returns list of lags and list of autocorrelation values for each lag, given the input 1D array
    """
    lags = np.arange(0, len(ring_data), 1)
    autocorrelation_normalized = [autocorrelate_single_value(ring_data,lag) for lag in range(0, len(ring_data))]
    if plot == True:
        plt.figure(figsize=(20, 10), dpi=80)
        plt.plot(lags, autocorrelation_normalized)
        plt.ylabel('Normalized autocorrelation')
        plt.xlabel('lag (pixels)')
        plt.show()
    return np.array(lags), np.array(autocorrelation_normalized)


