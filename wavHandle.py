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

    ax = plt.gca()  # 轴的编辑器
    ax.spines["right"].set_color("none")  # 将right的边隐藏
    ax.spines["top"].set_color("none")
    ax.spines["left"].set_position(("data", 0))  # 将left设置到0位置
    ax.spines["bottom"].set_position(("data", 0))

    plt.plot(freqArray, dB, color='k')
    plt.xlabel('Frequency (kHz)')
    plt.ylabel('Power (dB)')

    a = np.where(dB == np.max(dB))[0][0]

    plt.plot([freqArray[a], freqArray[a]], [0, np.max(dB)], "y", linewidth=1, linestyle="--")

    x = np.linspace(0, 200, 200, endpoint=True)
    y = np.linspace(3, 3, 200, endpoint=True)
    plt.plot(x, y, color="blue", linewidth=2.0, linestyle="--", alpha=0.5)

    plt.annotate((freqArray[a], np.max(dB)), xy=(freqArray[a], np.max(dB)), xycoords="data", xytext=(+10, +30),
                 textcoords="offset points",
                 arrowprops=dict(arrowstyle="->", connectionstyle="arc3, rad = .2"))

    plt.annotate("y=3dB", xy=(200, 3), xycoords="data", xytext=(+10, +20),
                 textcoords="offset points",
                 arrowprops=dict(arrowstyle="->", connectionstyle="arc3, rad = .2"))

    plt.scatter(freqArray, dB, c='r', alpha=.5)

    plt.show()

    print(freqArray[a], np.max(dB))

    print(np.where(dB == np.max(dB) / 2)[0])


if __name__ == '__main__':
    main()
