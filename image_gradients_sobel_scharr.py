

"""
  image_gradients_sobel_scharr.py
 
   sobel and Scharr Edge detector.

   USAGE:
     python image_gradients_sobel_scharr.py -i coinso1.png -s 0

"""
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, required=True,
                help="path to input image")
ap.add_argument("-s", "--scharr", type=int, default=0,
                help="path to input image")
args = vars(ap.parse_args())

'''Read and convert Image to gray scale'''
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray", gray)

''' use Scharr is arg is Sharrr else use sobel'''
ksize = -1 if args["scharr"] > 0 else 3
gX = cv2.Sobel(gray, ddepth=cv2.CV_32F, dx=1, dy=0, ksize=ksize)
gY = cv2.Sobel(gray, ddepth=cv2.CV_32F, dx=0, dy=1, ksize=ksize)

"""
  convert gx and gy values from floating point representation to unsigned int(8-bit)
"""

gX = cv2.convertScaleAbs(gX)

gY = cv2.convertScaleAbs(gY)

'''  combine the gradient representations '''
combined = cv2.addWeighted(gX, 0.5, gY, 0.5, 0)
''' show our output images '''
cv2.imshow("Sobel/Scharr X", gX)
cv2.imshow("Sobel/Scharr Y", gY)
cv2.imshow("Sobel/Scharr Combined", combined)
cv2.waitKey(0)
