
import argparse
ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image',
                default="image.jpg",
                help="path to image",
                type=str)
args = vars(ap.parse_args())
print(ap)
print(ap.parse_args())
print(args)
