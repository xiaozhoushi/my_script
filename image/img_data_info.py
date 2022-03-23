import numpy as np
from PIL import Image


def main():
    input_path = '/Users/Documents/data/GIANA_challenge/segmentation/SegmentationTrainingUpload/masks/1.bmp'
    img = Image.open(input_path)
    print(len(img.split()))
if __name__ == '__main__':
    main()
