import argparse
import os
import cv2
import numpy as np


def flip(image):
    flipped_image = np.fliplr(image)
    return flipped_image


ap = argparse.ArgumentParser()
ap.add_argument("--input", required=True, type=str)
args = ap.parse_args()

input_dir = "C://ProgramData/" + args.input + '/'
output_dir = 'C://ProgramData/aug_' + args.input + '/'
if not os.path.isdir(output_dir):
    print("no such dir")
    os.mkdir(output_dir)

files = os.listdir(input_dir)

print(files)

for img_name in files:
    img_path = input_dir + img_name
    img = cv2.imread(img_path)
    img_flip = flip(img)
    cv2.imwrite(output_dir + img_name[:-4] + '_flip.jpg', img_flip)
