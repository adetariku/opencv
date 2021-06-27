"""
   Morphological Operations.
         
    USAGE : python morphological.py --image opencv.jpg -m 0
          

"""

'''  import the necessary packages   '''


'''  construct the argument parser and parse the arguments '''
import argparse
import cv2
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
                help="path to input image")

ap.add_argument("-m", "--moperationCode", required=True,
                type=int,
                help="type of morphological operations \
                    (0=eroding, 1=dialating, \
                    2=opening,3=closing,4=blackhat,5=whitehat)")


args = vars(ap.parse_args())

''' load and convert image to grayscale '''

image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original", image)


def dilating(image):
    ''' apply a series of dilations '''
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    for i in range(0, 3):
        dilated = cv2.dilate(gray.copy(), None, iterations=i + 1)
        cv2.imshow("Dilated {} times".format(i + 1), dilated)
        cv2.waitKey(0)
    cv2.destroyAllWindows()

    return dilated


def eroding(image):
    ''' load the image, convert it to grayscale, and display it to our
        screen
    '''
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ''' apply a series of erosions '''
    for i in range(0, 3):
        eroded = cv2.erode(gray.copy(), None, iterations=i + 1)
        cv2.imshow("Eroded {} times".format(i + 1), eroded)
        cv2.waitKey(0)

    return eroded


def opening(image):
    ''' 
        An opening is an erosion followed by a dilation.

    '''
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    kernelSizes = [(3, 3), (5, 5), (7, 7)]
    '''  loop over the kernels sizes '''
    for kernelSize in kernelSizes:
        '''
           construct a rectangular kernel from the current size and then
           apply an "opening" operation
        '''
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernelSize)
        opening = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel)
        cv2.imshow("Opening: ({}, {})".format(
            kernelSize[0], kernelSize[1]), opening)
        cv2.waitKey(0)

    cv2.destroyAllWindows()

    return opening


def closing(image):
    '''The exact opposite to an opening would be a closing. 
       A closing is a dilation followed by an erosion.
    '''
    kernelSizes = [(3, 3), (5, 5), (7, 7)]
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    for kernelSize in kernelSizes:
        ''' construct a rectangular kernel form the current size, but this
            time apply a "closing" operation
        '''
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernelSize)
        closing = cv2.morphologyEx(gray, cv2.MORPH_CLOSE, kernel)

        cv2.imshow("Closing: ({}, {})".format(
            kernelSize[0], kernelSize[1]), closing)

        cv2.waitKey(0)

    return closing


def gradient(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    kernelSizes = [(3, 3), (5, 5), (7, 7)]
    for kernelSize in kernelSizes:
        ''' construct a rectangular kernel and apply a "morphological
           gradient" operation to the image
        '''
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernelSize)
        gradient = cv2.morphologyEx(gray, cv2.MORPH_GRADIENT, kernel)
        cv2.imshow("Gradient: ({}, {})".format(
            kernelSize[0], kernelSize[1]), gradient)
        cv2.waitKey(0)

    return gradient


def blackhat(image):
    ''' load the image and convert it to grayscale '''
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ''' construct a rectangular kernel (13x5) and apply a blackhat
        operation which enables us to find dark regions on a light
        background

        why (13x5) usually a plate is 3 times wide than it is tall
    '''
    rectKernel = cv2.getStructuringElement(cv2.MORPH_RECT, (13, 5))
    blackhat = cv2.morphologyEx(gray, cv2.MORPH_BLACKHAT, rectKernel)
    ''' show the output images '''
    cv2.imshow("Original", image)
    cv2.imshow("Blackhat", blackhat)
    cv2.waitKey(0)

    return blackhat


def whitehat(image):
    ''' similarly, a tophat (also called a "whitehat") operation will
       enable us to find light regions on a dark background
    '''
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    rectKernel = cv2.getStructuringElement(cv2.MORPH_RECT, (13, 5))
    tophat = cv2.morphologyEx(gray, cv2.MORPH_TOPHAT, rectKernel)
    ''' show the output images '''
    cv2.imshow("Original", image)
    cv2.imshow("Tophat", tophat)
    cv2.waitKey(0)

    return tophat


if args["moperationCode"] == 0:
    print("eroding")
    eroding(image)

elif args["moperationCode"] == 1:
    print("dialation")
    dilating(image)

elif args["moperationCode"] == 2:
    print("opening")
    opening(image)

elif args["moperationCode"] == 3:
    print("closing")
    closing(image)
elif args["moperationCode"] == 4:
    print("black hat")
    blackhat(image)
elif args["moperationCode"] == 5:
    print("white hat")
    whitehat(image)
