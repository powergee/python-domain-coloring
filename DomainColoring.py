import matplotlib.pyplot as plt
import matplotlib.colors as color
import numpy as np
import mpmath as mp
import time

def getSimpleHSV(mapped):
    H = ((np.angle(mapped) + 2.*np.pi) % (2.*np.pi)) / (2.*np.pi)
    S = np.ones(mapped.shape)
    V = (2/np.pi) * np.arctan(np.abs(mapped))
    return (H, S, V)

def getHSVToFindSolutions(mapped):
    H = ((np.angle(mapped) + 2.*np.pi) % (2.*np.pi)) / (2.*np.pi)
    S = np.reciprocal(1. + 0.3*np.log(np.abs(mapped)+1.))
    V = 1. - np.reciprocal(1.1 + 5.*np.log(np.abs(mapped)+1.))
    return (H, S, V)

def showPlot(func, colorFunc, rMin, rMax, rCount, iMin, iMax, iCount):
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

    (H, S, V) = colorFunc(mapped)
    resultImage = color.hsv_to_rgb(np.dstack((H, S, V)))
    plt.imshow(resultImage)
    plt.gca().invert_yaxis()
    plt.gca().get_xaxis().set_visible(False)
    plt.gca().get_yaxis().set_visible(False)
    plt.show()

showPlot(lambda z: z, getSimpleHSV, -3, 3, 1000, -3, 3, 1000)
showPlot(lambda z: z**3-1, getSimpleHSV, -3, 3, 1000, -3, 3, 1000)
# showPlot(mp.zeta, getHSVToFindSolutions, -30, 30, 500, -30, 30, 500)
# showPlot(mp.zeta, getHSVToFindSolutions, -5, 5, 100, 0, 100, 1000)