"""

    USAGE
    python python gradient_magnitude_and_orientation.py  --image coins01.png"

"""
import matplotlib.pyplot as plt
import numpy as np
import argparse
import cv2


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, required=True,
                help="path to input image")
args = vars(ap.parse_args())


''' Load the input image '''
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


def gradX(gray):
    ''' Gradient along the x-axis'''
    gX = cv2.Sobel(gray, cv2.CV_64F, 1, 0)

    return gX


def gradY(gray):
    ''' Gradient along the y-axis'''
    gX = cv2.Sobel(gray, cv2.CV_64F, 0, 1)

    return gX


def gradMagnitude(gX, gY):
    ''' compute image gradients'''
    magnitude = np.sqrt((gX ** 2) + (gY ** 2))

    return magnitude


def gradOrientation(gX, gY):
    ''' Compute image Orientation'''
    direction = np.arctan2(gY, gX)*(180/np.pi) % 180

    return direction


def displayResults(gray, magnitude, orientation):

    (fig, axs) = plt.subplots(nrows=1, ncols=3, figsize=(8, 4))

    ''' plot images '''
    axs[0].imshow(gray, cmap="gray")
    axs[1].imshow(magnitude, cmap="jet")
    axs[2].imshow(orientation, cmap="jet")

    ''' set the titles of each axes '''
    axs[0].set_title("Grayscale")
    axs[1].set_title("Gradient Magnitude")
    axs[2].set_title("Gradient Orientation [0, 180]")

    ''' turn off the x and y ticks '''
    for i in range(0, 3):
        axs[i].get_xaxis().set_ticks([])
        axs[i].get_yaxis().set_ticks([])

    ''' show the plots '''
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    gX = gradX(gray)
    gY = gradY(gray)
    magnitude = gradMagnitude(gX, gY)
    orient = gradOrientation(gX, gY)
    displayResults(gray, magnitude, orient)
