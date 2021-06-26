"""
  Image Rotation Functions.
   1. cv2.rotate : [cv2.getRotationMatrix2D and cv2.warpAffine]
          requires explicit a translation matrix followed by explicit warping

   2. imutils.rotate : uses opencv but can be made using a single function call

   3. imutils.rotate_bound : ensurs no part of the image is cut of during rotation
   
   Rotation matrix:
   M = is a 2 by 2 matrix
   R=I*M, Rotated Image, R is the product of the original image, I and the rotation Matrix M.


 USAGE : python image_rotation.py  --image opencv.jpg --center 10 50

 NOTE THE SPACE BETWEEN 10 AND 50.

 REFERENCE: PyImagesearch.com

"""

'''  import the necessary packages '''
'''  construct the argument parser and parse the arguments '''

''' argument parser '''
import argparse
import imutils
import cv2
import numpy as np
ap = argparse.ArgumentParser()

ap.add_argument("-i", "--image",
                type=str,
                required=True,
                help="path to the input image"
                )

ap.add_argument("-a", "--angle",
                type=float,
                default=0,
                help="angle of rotation around image center"
                )

ap.add_argument("-c", "--center",
                type=int, default=None, nargs='+',
                help="Center of Image rotation")

args = vars(ap.parse_args())
''' load the image '''
image = cv2.imread(args["image"])
cv2.imshow("Original", image)

(h, w) = image.shape[:2]
if args["center"] is None:
    (cX, cY) = (w // 2, h // 2)
else:
    (cX, cY) = tuple(args["center"])
    (cX, cY) = (int(cX), int(cY))

angle = np.float32(args["angle"])
''' rotate image by <<angle>> degrees around the image center '''
M = cv2.getRotationMatrix2D((cX, cY), angle, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.putText(rotated, f"rotated by {angle} degress",
            (50, 50), cv2.FONT_HERSHEY_COMPLEX, 0.75, (0, 0, 255))
cv2.imshow("Rotated by 45 Degrees", rotated)


'''  use our imutils function to rotate an image 180 degrees '''
rotated = imutils.rotate(image, angle)
cv2.imshow(f"Rotated by {angle} degress around center=({cX,cY})", rotated)
'''
    rotate image by <<angle>> degrees, ensuring the entire rotated image still 
    renders within the viewing area '''

rotated = imutils.rotate_bound(image, angle)
cv2.imshow("Rotated Without Cropping", rotated)
cv2.waitKey(7000)
