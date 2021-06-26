"""
  image_resize.py 
      resizes an image.


"""

'''  import the necessary packages '''
'''  construct the argument parser and parse the arguments '''

import argparse
import imutils
import cv2
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, required=True,
                help="path to the input image")

ap.add_argument("-w", "--width", type=int, default=None,
                help="width of the resized image")

ap.add_argument("-l", "--height", type=int, default=None,
                help="height of the resized image")

args = vars(ap.parse_args())


''' load the original input image and display it on our screen '''
image = cv2.imread(args["image"])
cv2.imshow("Original", image)


if args["width"] is not None:
    scale = args["width"]/image.shape[1]
    dim = (args["width"], int(image.shape[0]*scale))

elif args["height"] is not None:
    scale = args["height"]/image.shape[0]
    dim = (int(image.shape[1]*scale), args["height"])

else:
    scale = 1.0
    dim = (image.shape[1], image.shape[0])

print("dim ", dim)
'''  perform the actual resizing of the image   '''
resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
cv2.putText(resized, f"(w,h)={dim}", (50, 50),
            cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 0.75, (255, 0, 0), 1)
cv2.imshow("Resized (Width)", resized)
cv2.waitKey(2000)
