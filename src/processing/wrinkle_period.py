import numpy as np
import matplotlib.pyplot as plt

from scipy.ndimage import gaussian_filter
from scipy.signal import find_peaks

from src.processing.autocorrelation import autocorrelate_radial_ring
from src.processing.radial import create_radius_select_stack


def find_period_autocorrelation_fft(autocorrelation, gaussian_sigma = 1, plot=False):
    """
    Finds the dominant period of the autocorrelation function for a given smoothing,
    using the fast fourier transform
    """
    fs = 2
    d = 1/fs
    n = autocorrelation.size
    fft_autocorrelation = np.fft.fft(autocorrelation) #find autocorrelation
    fft_freqs = (np.fft.fftfreq(n, d)*n*d) #find frequencies

    length = round(len(fft_freqs*n*d)/2)

    #take only first half of values
    fft_autocorrelation = fft_autocorrelation[0:length]
    fft_freqs = fft_freqs[0:length]

    fft_autocorrelation = gaussian_filter((fft_autocorrelation.real), gaussian_sigma)

    peaks, peak_heights = find_peaks(fft_autocorrelation, 0.5*np.max(fft_autocorrelation))
    print('no peaks = ', len(peaks))

    #if more than 8 peaks above 0.5 times max fft amp, then set period to zero
    if len(peaks) > 8:
        period = [0]
        period_deg = [0]
    else:
        #find frequency at which max peak occurs and label as period of wrinkles
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



def periods_from_image(image, circle_radius, circle_centre, tolerance=0.5):
    """
    Returns period in pixels and degrees given an input image and circle radius
    """
    stack = create_radius_select_stack(image, circle_centre,  circle_radius, tolerance)
    data = stack[2]
    lags, autocorrelation = autocorrelate_radial_ring(data)
    period_pixels, period_deg = find_period_autocorrelation_fft(autocorrelation, 0.8)
    return period_pixels, period_deg


def periods_multiple_radii(image, centre_fitted, start_radius, stop_radius, step, plot=False):
    """
    Finds periods for a range of given radii for a certain image and plots them if required
    """
    period  = []
    radii = []
    for r in range(round(start_radius),round(stop_radius), step):
        radii.append(r)
        period_pixels, period_deg = periods_from_image(image, r, centre_fitted)
        period.append(period_deg)
    if plot == True:
        plt.figure(figsize=(20, 10), dpi=80)
    plt.plot(radii, period)
    plt.xlabel('Radius (no.pixels)')
    plt.ylabel('Period (degrees)')

    return radii, period