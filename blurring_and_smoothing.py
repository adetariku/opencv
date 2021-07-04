"""
  Image blurring and smoothing

  USAGE: 


"""

import argparse
import cv2
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="adrian.png",
                help="path to input image")

ap.add_argument("-m", "--blurTypeCode", required=True,
                type=int,
                help="type of morphological operations \
                    (0=averaging, 1=median, \
                    2=Gaussian,3=bilateral)")


args = vars(ap.parse_args())
''' load the image, display it '''
image = cv2.imread(args["image"])
cv2.imshow("Original", image)


def averageFilter(image):
    kernelSizes = [(3, 3), (9, 9), (15, 15)]
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ''' loop over the kernel sizes '''
    for (kX, kY) in kernelSizes:
        ''' apply an "average" blur to the image using the current kernel
            size
        '''
        blurred = cv2.blur(image, (kX, kY))
        cv2.imshow("Average ({}, {})".format(kX, kY), blurred)
        cv2.waitKey(0)

    return blurred


def gaussianb(image):
    '''loop over the kernel sizes again '''
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    kernelSizes = [(3, 3), (9, 9), (15, 15)]
    for (kX, kY) in kernelSizes:
        ''' apply a "Gaussian" blur to the image'''
        blurred = cv2.GaussianBlur(image, (kX, kY), 0)
        cv2.imshow("Gaussian", blurred)
        cv2.waitKey(0)

    return blurred


def medianfilter(image):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = []

    for k in (3, 9, 15):
        ''' apply a "median" blur to the image '''
        blurred = cv2.medianBlur(image, k)
        cv2.imshow("Median {}".format(k), blurred)
        cv2.waitKey(0)

    return blurred


def bilateral(image):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    params = [(11, 21, 7), (11, 41, 21), (11, 61, 39)]
    blurred = []
    '''  loop over the diameter, sigma color, and sigma space '''
    for (diameter, sigmaColor, sigmaSpace) in params:
        ''' 
            apply bilateral filtering to the image using the current set of
            parameters
        '''
        blurred = cv2.bilateralFilter(image, diameter, sigmaColor, sigmaSpace)
        '''  show the output image and associated parameters  '''
        title = "Blurred d={}, sc={}, ss={}".format(
                diameter, sigmaColor, sigmaSpace)
        cv2.imshow(title, blurred)
        cv2.waitKey(1500)

    return blurred


averageFilter(image)
bilateral(image)
medianfilter(image)
gaussianb(image)
