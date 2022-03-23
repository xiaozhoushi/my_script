import os
import sys
import pydicom
from PIL import Image

import numpy as np
import cv2

from multiprocessing import Pool

def get_start_end(array, y1, y2):
    for i in range(len(array)):
        if array[i] > 125:
            y1 = min(y1, i)
            y2 = max(y2, i)
    return y1, y2

def crop(path, path_mask, out_img, out_mask):
    img = Image.open(path)
    img_mask = img.convert('L')
    img_mask = np.array(img_mask)
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

    mask = Image.open(path_mask).convert('L')
    crop = img.crop((x1,y1,x2,y2)) 
    crop_mask = mask.crop((x1,y1,x2,y2))
    crop.save(out_img)
    crop_mask.save(out_mask)


def crop1(path_in, input_mask_dir, path_out_dir):
    name = os.path.basename(path_in)
    mask_path = os.path.join(input_mask_dir, name) 
    out_img = os.path.join(path_out_dir, 'images', name)
    out_mask = os.path.join(path_out_dir, 'masks', name)
    crop(path_in, mask_path, out_img, out_mask )
    print(path_in, flush=True)

if __name__ == '__main__':
    pool = Pool(processes=6)
    input_dir = '/Users/Documents/data/GIANA_challenge/segmentation/test/cvc612/images'
    input_mask_dir = '/Users/Documents/data/GIANA_challenge/segmentation/test/cvc612/masks'
    out_dir = '/Users/Documents/data/GIANA_challenge/segmentation/test_crop/cvc612_crop'
    img_list = [os.path.join(input_dir, item) for item in os.listdir(input_dir) if '.png' in item]
    if not os.path.exists(os.path.join(out_dir, 'images')):
        os.makedirs(os.path.join(out_dir, 'images'))
    if not os.path.exists(os.path.join(out_dir, 'masks')):
        os.makedirs(os.path.join(out_dir, 'masks'))
    print(len(img_list))
    for img_path in img_list:
        #crop1(img_path, input_mask_dir, out_dir)
        pool.apply_async(crop1, [img_path, input_mask_dir, out_dir])

    pool.close()
    pool.join()
