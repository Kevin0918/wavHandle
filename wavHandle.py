# -*- coding: utf-8 -*-

import numpy as np
import pylab as py
import matplotlib.pyplot as plt
from scipy.io import wavfile


def main():
    fs, data = wavfile.read('/Users/kevin/Documents/MATLAB/20141221_211337_021.wav')

    shape = float(data.shape[0])
    timeArray = np.arange(0, shape, 1)
    timeArray = timeArray / fs
    timeArray = timeArray * 1000

    plt.figure(1)
    plt.plot(timeArray, data, color='k')
    plt.xlabel('Time(ms)')
    plt.ylabel('Amplitude')

    p = py.fft(data)
    n = len(data)

    nUniquePts = int(np.ceil((n + 1) / 2.0))
    p = p[0:nUniquePts]
    p = abs(p)
    p = p / float(n)
    p = p ** 2
    if n % 2 > 0:
        p[1:len(p)] = p[1:len(p)] * 2
    else:
        p[1:len(p) - 1] = p[1:len(p) - 1] * 2
    freqArray = np.arange(0, nUniquePts, 1.0) * (fs / n);
    freqArray = freqArray / 1000
    dB = 10 * (np.log10(p))

    # plt.figure(2)
    # plt.plot(timeArray, 10*(np.log10(p)), color='k')
    # plt.xlabel('Time(ms)')
    # plt.ylabel('Power (dB)')

    plt.figure(2)
    plt.plot(freqArray, dB, color='k')
    plt.xlabel('Frequency (kHz)')
    plt.ylabel('Power (dB)')

    a = np.where(dB == np.max(dB))[0][0]

    plt.annotate((freqArray[a], np.max(dB)), xy=(freqArray[a], np.max(dB)), xycoords="data", xytext=(+10, +30),
                 textcoords="offset points",
                 arrowprops=dict(arrowstyle="->", connectionstyle="arc3, rad = .2"))

    plt.show()

    print(freqArray[a], np.max(dB))

    print(np.where(dB == np.max(dB) / 2)[0])


if __name__ == '__main__':
    main()
