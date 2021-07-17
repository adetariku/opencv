

"""
	USAGE
	     python grayscale_histogram.py --image beach.png


"""

from matplotlib import pyplot as plt
import argparse
import cv2

'''  construct the argument parser and parse the arguments '''
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
                help="path to the image")
args = vars(ap.parse_args())
image = cv2.imread(args["image"])


def img2gray(image):

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    return gray


def calHistogram(image):
    '''images, channels, mask, histSize, range '''
    hist = cv2.calcHist([image], [0], None, [256], [0, 256])
    return hist


def ploting(image):

    plt.figure()
    plt.axis("off")

    plt.imshow(cv2.cvtColor(image, cv2.COLOR_GRAY2RGB))
    plt.show()


def plotHist(hist, title):
    plt.figure()
    plt.title(title)
    plt.xlabel("Bins")
    plt.ylabel("# of Pixels")
    plt.plot(hist)
    plt.xlim([0, 256])
    plt.show()


gray = img2gray(image)
hist = calHistogram(image)
# ploting(gray)
title = "Grayscale Histogram"
plotHist(hist, title)
hist /= hist.sum()
plotHist(hist, "normalized")
