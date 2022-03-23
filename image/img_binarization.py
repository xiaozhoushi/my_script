from PIL import Image
import numpy as np
import glob
import os


def main():
    file_path = '/Users/Documents/data/colonoscopy_images/seg_resize_512/mask_file_test'
    threshold = 0
    all_img = glob.glob(file_path + '/*.jpg')
    for img_path in all_img:
        img = Image.open(img_path) 
        img = np.array(img)
        img[img > threshold] = 255
        img = Image.fromarray(img.astype(np.uint8))
        img.save(img_path)
        print('process: ', img_path)

if __name__ == '__main__':
    main()
