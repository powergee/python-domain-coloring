import matplotlib.pyplot as plt
import matplotlib.colors as color
import numpy as np
import mpmath as mp
import time

def showPlot(func, rMin, rMax, rCount, iMin, iMax, iCount):
    realSamples = np.linspace(rMin, rMax, rCount)
    imgSamples = np.linspace(iMin, iMax, iCount)
    realPositions, imgPositions = np.meshgrid(realSamples, imgSamples)

    mapped = None
    try:
        # efficient
        mapped = func(realPositions + 1j*imgPositions)
    except:
        # inefficient but works with almost all types of func
        mapped = realPositions + 1j*imgPositions
        rows = mapped.shape[0]
        cols = mapped.shape[1]
        for r in range(0, rows):
            for c in range(0, cols):
                mapped[r, c] = func(mapped[r, c])

    H = ((np.angle(mapped) + 2.*np.pi) % (2.*np.pi)) / (2.*np.pi)
    S = np.reciprocal(1. + 0.3*np.log(np.abs(mapped)+1.))
    V = 1. - np.reciprocal(1.1 + 5.*np.log(np.abs(mapped)+1.))

    resultImage = color.hsv_to_rgb(np.dstack((H, S, V)))
    plt.imshow(resultImage)
    plt.gca().invert_yaxis()
    plt.gca().get_xaxis().set_visible(False)
    plt.gca().get_yaxis().set_visible(False)
    plt.show()

showPlot(lambda z: z**3-1, -3, 3, 1000, -3, 3, 1000)
#showPlot(mp.zeta, -10, 10, 500, -10, 10, 500)