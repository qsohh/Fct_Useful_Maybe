
# import public modules
import os
import numpy as np
import scipy.signal as sg


# definition of fonctions for the Butterworth bandpass filter
def butter_bandpass(lowcut, highcut, fs, order=5):
    '''
    Fonction butter_bandpass(lowcut, highcut, fs, order=5)
    Input :  lowcut : lowcut frequence
             highcut : highcut frequence
             fs : frequence d echantillonnage
             order : order of the filter
    Output : b
             a
    '''
    nyq = 0.5 * fs  # Nyquist frequency
    low = lowcut / nyq  # normalized by Nyquist frequency
    high = highcut / nyq  # normalized by Nyquist frequency
    b, a = sg.butter(order, [low, high], btype='band')
    return b, a


def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = sg.lfilter(b, a, data)
    return y


# definition of fonctions of the Butterworth highpass filter
def butter_highpass(lowcut, fs, order=5):
    '''
    Fonction : butter_highpass(highcut, fs, order=5)
    Input :  highcut : highcut frequence
             fs : frequence d echantillonnage
             order : order of the filter
    Output : b
             a
    '''
    nyq = 0.5 * fs
    low = lowcut / nyq
    b, a = sg.butter(order, low, btype='high')
    return b, a


def butter_highpass_filter(data, lowcut, fs, order=5):
    b, a = butter_highpass(lowcut, fs, order=order)
    y = sg.lfilter(b, a, data)
    return y


# normal DFT
def dft(s):
    '''
    Fonction : dft(s)
    Input : s : signal to be 'TF'ed
    Output : S : the DFT of s
    '''
    N = len(s)
    k = np.arange(N)
    return np.dot(s, np.exp(-2j * np.pi * k * k[:, np.newaxis] / N))


# DFT frequences
def dftfreq(n, d):
    '''
    Fonction : dftfreq(n, d)
    Input : n : length of the signal
            d : step of sampling
    Output : F : the frequences
    '''
    return np.fft.fftfreq(n, d)


# Call a Python script
def CallScript(filename, path=''):
    '''
    Fonction : CallScription(filename, path='')
    Input : filename
            path
    Output : None
    '''
    with open(os.path.join(filename)) as f:
        exec(f.read())
