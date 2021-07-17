"""
    Calaulate Historgrams of color images
	USAGE
	    python color_histograms.py --image beach.png

"""
from matplotlib import pyplot as plt
import argparse
import imutils
import cv2

'''
	construct the argument parser and parse the arguments


'''


def scan_args():
    '''Scan Arguments'''
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True,
                    help="path to the image")
    args = vars(ap.parse_args())

    return args


def splitImgChannels(image):
    '''Split color image into its channels'''
    channels = cv2.split(image)

    return channels


def ploting(image, title):
    plt.figure()
    plt.axis("off")
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_GRAY2RGB))
    plt.title(title)
    plt.show()


def plotHist(channels, colors, grayed=False):
    '''draw a histogram for each channel'''
    for (channel, color) in zip(channels, colors):
        hist = cv2.calcHist([channel], [0], None, [256], [0, 256])
        plt.plot(hist, color=color)
        plt.xlim([0, 256])

    if grayed:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        hist = cv2.calcHist([gray], [0], None, [256], [0, 256])
        plt.plot(hist, color="gray")
        plt.legend(labels=["BLUE", "GREEN", "RED", "GRAY SCALE"])
    else:
        plt.legend(labels=["BLUE", "GREEN", "RED"])

    plt.show()


def draw2DColorHist(chans):
    ''' 
        INPUT: BGR color image
            create a new figure and then plot a 2D color histogram for the
        green and blue channels
    '''

    fig = plt.figure()
    ax = fig.add_subplot(131)
    hist = cv2.calcHist([chans[1], chans[0]], [0, 1], None, [32, 32],
                        [0, 256, 0, 256])
    p = ax.imshow(hist, interpolation="nearest")
    ax.set_title("2D Color Histogram for G and B")
    plt.colorbar(p)

    '''  plot a 2D color histogram for the green and red channels '''
    ax = fig.add_subplot(132)
    hist = cv2.calcHist([chans[1], chans[2]], [0, 1], None, [32, 32],
                        [0, 256, 0, 256])
    p = ax.imshow(hist, interpolation="nearest")
    ax.set_title("2D Color Histogram for G and R")
    plt.colorbar(p)

    ''' plot a 2D color histogram for blue and red channels'''
    ax = fig.add_subplot(133)
    hist = cv2.calcHist([chans[0], chans[2]], [0, 1], None, [32, 32],
                        [0, 256, 0, 256])
    p = ax.imshow(hist, interpolation="nearest")
    ax.set_title("2D Color Histogram for B and R")
    plt.colorbar(p)

    plt.show()


def plot3DHist(image):
    ''' Draw a histogram for the 3 channels'''
    hist = cv2.calcHist([image], [0, 1, 2],
                        None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
    print("3D histogram shape: {}, with {} values".format(
        hist.shape, hist.flatten().shape[0]))

    ''' display the original input image '''
    plt.figure()
    plt.axis("off")
    plt.imshow(imutils.opencv2matplotlib(image))
    plt.show()


if __name__ == '__main__':
    args = scan_args()
    ''' load the input image from disk '''
    image = cv2.imread(args["image"])
    channels = splitImgChannels(image)
    colors = ['BLUE', 'GREEN', 'RED']
    plotHist(channels, colors)
    plotHist(channels, colors, True)
    draw2DColorHist(channels)
    plot3DHist(image)
