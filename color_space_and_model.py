
"""



"""
"""
   USAGE:
       python color_space_and_model.py --image opencv.jpg

"""


''' construct the argument parser and parse the arguments '''

import argparse
import cv2
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="opencv.jpg",
                help="path to input image")
args = vars(ap.parse_args())
''''  load the original image and show it '''
image = cv2.imread(args["image"])
cv2.imshow("RGB", image)


def bgr2gray(image):
    if image.shape[2] == 3:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    else:
        gray = image

    return gray


def gaussianBlur(gray):

    blurred = cv2.GaussianBlur(gray, (7, 7), 0)

    return blurred


def otsuBlurring(gray):

    (T, threshInv) = cv2.threshold(
        blurred, 0, 255,
        cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)

    return threshInv


def adaptiveThBlur(gray):

    thresh = cv2.adaptiveThreshold(gray, 255,
                                   cv2.ADAPTIVE_THRESH_MEAN_C,
                                   cv2.THRESH_BINARY_INV, 21, 10)

    return thresh


def splitBGR(image):
    for (name, chan) in zip(("B", "G", "R"), cv2.split(image)):
        cv2.imshow(name, chan)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def splitHSV(imageBGR):
    hsv = cv2.cvtColor(imageBGR, cv2.COLOR_BGR2HSV)
    cv2.imshow("HSV", hsv)
    '''  loop over each of the individual channels and display them '''
    for (name, chan) in zip(("H", "S", "V"), cv2.split(hsv)):
        cv2.imshow(name, chan)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def plotting(image, title):
    cv2.imshow(title, image)
    cv2.waitKey(1500)


def splitLAB(image):
    ''' convert the image to the L*a*b* color space and show it'''
    lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
    cv2.imshow("L*a*b*", lab)
    for (name, chan) in zip(("L*", "a*", "b*"), cv2.split(lab)):
        cv2.imshow(name, chan)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


''' show the original and grayscale versions of the image '''

gray = bgr2gray(image)
cv2.imshow("Original", image)
cv2.imshow("Grayscale", gray)

gaussian = gaussianBlur(gray)
plotting(gaussian, "Gaussian")
adaptive = adaptiveThBlur(gray)
plotting(adaptive, "Adaptive")
splitBGR(image)
splitHSV(image)
splitLAB(image)
