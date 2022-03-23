import numpy as np
import os
import glob
import shutil
import copy
import cv2

def main():
    path_source = '/Users/Documents/data/GIANA_challenge/segmentation/test/hdtest'
    path_target = '/Users/Documents/data/GIANA_challenge/class/temp/images'
    path_mask = '/Users/Documents/data/GIANA_challenge/class/temp/masks'
    out_dir = '/Users/Documents/data/GIANA_challenge/segmentation/match'

    source_list = glob.glob(path_source + '/*.tif')
    target_list = glob.glob(path_target + '/*.tif')
    for path_img in source_list:
        source_img = cv2.imread(path_img)
        source_img = cv2.cvtColor(source_img, cv2.COLOR_BGR2GRAY)
        s_h, s_w = source_img.shape
        source_arr = np.array(source_img)
        target_find = None
        min_val = float('inf')

        start_w, end_w = s_w // 2 - 20, s_w // 2 + 20
        start_h, end_h = s_h // 2 - 20, s_h // 2 + 20
        source_arr = source_arr[start_h:end_h, start_w:end_w]


        for path_img_t in target_list:
            target_img = cv2.imread(path_img_t)
            target_img = cv2.cvtColor(target_img, cv2.COLOR_BGR2GRAY)
            t_h, t_w = target_img.shape
            if s_w != t_w or s_h != t_h:
                continue
            target_arr = np.array(target_img)
            target_arr = target_arr[start_h:end_h, start_w:end_w]
            array = np.abs(source_arr - target_arr)
            val = np.mean(array)
            if val < min_val:
                min_val = val
                target_find = path_img_t

        name = os.path.basename(path_img)
        shutil.copy(path_img, os.path.join(out_dir, name)) 

        if target_find is not None:
            name_match = name.split('.')[0] + '_t.tif'
            shutil.copy(target_find, os.path.join(out_dir, name_match))

            target_mask_name = os.path.basename(target_find)
            ori_mask_path = os.path.join(path_mask, target_mask_name)
            target_save_name = name.split('.')[0] + '_mask.tif'
            shutil.copy(ori_mask_path, os.path.join(out_dir, target_save_name))
        
        print(path_img)



if __name__ == '__main__':
    main()

