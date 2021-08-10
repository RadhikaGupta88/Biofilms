import numpy as np
import matplotlib.pyplot as plt

from scipy.ndimage import gaussian_filter
from scipy.signal import find_peaks

from src.processing.constants import BUCKLING_PATH

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



def find_period_autocorrelation_fft(autocorrelation, gaussian_sigma = 1, plot=False):
    """
    Finds the dominant period of the autocorrelation function for a given smoothing,
    using the fast fourier transform
    """
    fs = 2
    d = 1/fs
    n = autocorrelation.size
    fft_autocorrelation = np.fft.fft(autocorrelation)
    fft_freqs = (np.fft.fftfreq(n, d)*n*d)

    length = round(len(fft_freqs*n*d)/2)

    fft_autocorrelation = fft_autocorrelation[0:length]
    fft_freqs = fft_freqs[0:length]

    fft_autocorrelation = gaussian_filter((fft_autocorrelation.real), gaussian_sigma)

    peaks, peak_heights = find_peaks(fft_autocorrelation, 0.5*np.max(fft_autocorrelation))
    print('no peaks = ', len(peaks))
    if len(peaks) > 6:
        period = [0]
        period_deg = [0]
    else:
        peak_heights = peak_heights['peak_heights']
        peak_index =  peaks[np.where(peak_heights == np.max(peak_heights))]
        period = fft_freqs[peak_index]
        period_deg = (period/len(autocorrelation))*360

    if plot == True:
        plt.figure(figsize = (20,10))
        plt.plot(fft_freqs, fft_autocorrelation, label='autocorrelation fourier transform')
        plt.plot(fft_freqs[peaks], fft_autocorrelation[peaks] ,'gx', label='peaks')
        plt.axvline(x=period, color='r', label='period', linestyle = 'dashed')
        #plt.plot(period, fft_autocorrelation[peak_index] , 'rx', label='period')
        plt.xlabel("Frequency (Hz)")
        plt.ylabel("Amplitude")
        plt.legend()
        plt.show()

    print(f'period = {period[0]} pixels, {period_deg[0]} degrees')
    print(np.shape(period_deg))

    return period[0], period_deg[0]

