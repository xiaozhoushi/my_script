import os
import sys
import pydicom

import cv2
import numpy as np

from multiprocessing import Pool

def get_start_end(array, y1, y2):
    for i in range(len(array)):
        if array[i] > 125:
            y1 = min(y1, i)
            y2 = max(y2, i)
    return y1, y2

def crop(path, out_img):
    img = cv2.imread(path)
    img_mask = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    threshold = np.mean(img_mask[:10,:10]) + 2
    img_mask = cv2.blur(img_mask, (5, 5))
    img_mask[img_mask < threshold] = 0
    img_mask[img_mask >= threshold] = 255
    h, w = img_mask.shape
    start, end = max(w//2 -20, 0), min(w//2 +20, w)
    
    y1, y2 = h, 0 
    for i in range(start, end):
        y1, y2 = get_start_end(img_mask[:, i], y1, y2)

    start, end = max(h//2 -20, 0), min(h//2 +20, h)
    x1, x2 = w, 0
    for i in range(start, end):
        x1, x2 = get_start_end(img_mask[i, :], x1, x2)

    crop = img[y1: y2, x1: x2]
    cv2.imwrite(out_img, crop)

def crop1(path_in, path_out_dir):
    name = os.path.basename(path_in)
    out_img = os.path.join(path_out_dir, name)
    crop(path_in, out_img)
    print(path_in, flush=True)

if __name__ == '__main__':
    pool = Pool(processes=6)
    input_dir = '/Users/Documents/data/GIANA_challenge/segmentation/test/hdtest'
    out_dir = '/Users/Documents/data/GIANA_challenge/segmentation/test_crop/hdtest_crop'
    img_list = [os.path.join(input_dir, item) for item in os.listdir(input_dir) if '.tif' in item]
    if not os.path.exists(out_dir):
        os.mkdir(out_dir)
    for img_path in img_list:
        #crop1(img_path, input_mask_dir, out_dir)
        pool.apply_async(crop1, [img_path, out_dir])

    pool.close()
    pool.join()
