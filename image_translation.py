
"""
  image_translation.py

  uses opencv for translating images. The steps are
    1. load image
    2. design translation matrix
    3. use the c2.warpAffine function to persorm the translation.

USAGE:  pythpn image_translation.py --image opencv.jpg -x 20 -y 30 
(to itranslate image opencv.jpg 20 pixels to the right and 30 pixels down.)

"""


# import the necessary packages
import numpy as np
import argparse
import imutils
import cv2


""" construct the argument parser and parse the arguments """
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="opencv_logo.png",
                help="path to the input image")

ap.add_argument("-x", "--shiftx",
                type=int,
                required=True,
                help="The number of shifts to x-direction")

ap.add_argument("-y", "--shifty",
                required=True,
                type=int,
                help="The number of shifts to y-direction")
args = vars(ap.parse_args())


image = cv2.imread(args["image"])
cv2.imshow("Original", image)


"""  shift the image 25 pixels to the right and 50 pixels down.

    M = np.float32([[1, 0, 25], [0, 1, 50]])

 """
M = np.float32(
    [
        [1, 0, args["shiftx"]],
        [0, 1, args["shifty"]],
    ])

shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
xx = args["shiftx"]
yy = args["shifty"]
cv2.putText(shifted, f"svector=({xx}, {yy})",
            (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255, 0, 0), 1)
cv2.imshow("Shifted Down and Right", shifted)
cv2.waitKey(850)
