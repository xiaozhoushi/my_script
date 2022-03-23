import numpy as np
import os
from PIL import Image
import glob
import shutil

def main():
    path_source = '/Users/Documents/data/GIANA_challenge/segmentation/test_crop/hdtest_crop'
    path_target = '/Users/Documents/data/GIANA_challenge/class/temp/images'
    out_dir = '/Users/Documents/data/GIANA_challenge/segmentation/match'


    orig_img = '/Users/Documents/data/GIANA_challenge/segmentation/test/hdtest'
    match_mask = '/Users/Documents/data/GIANA_challenge/class/temp/masks'
    out_match_ori = '/Users/Documents/data/GIANA_challenge/segmentation/match_ori'
    source_list = glob.glob(path_source + '/*.tif')
    target_list = glob.glob(path_target + '/*.tif')
    for path_img in source_list:
        source_img = Image.open(path_img)
        s_w, s_h = source_img.size
        source_arr = np.asarray(source_img)
        
        target = None
        target_find = None
        min_val = float('inf')
        for path_img_t in target_list:
            target_img = Image.open(path_img_t)
            t_w, t_h = target_img.size
            if s_w != t_w or s_h != t_h:
                continue
            target_arr = np.asarray(target_img)
            val = np.mean(np.abs(source_arr - target_arr))
            if val < min_val:
                min_val = val
                target = target_img 
                target_find = path_img_t
        name = os.path.basename(path_img)
        name_match = name.split('.')[0] + '_m.tif'
        source_img.save(os.path.join(out_dir, name)) 
        if target is not None:
            target.save(os.path.join(out_dir, name_match))

        ori_path = os.path.join(orig_img, name)
        shutil.copy(ori_path, os.path.join(out_match_ori, name))

        if target_find is not None:
            target_mask_name = os.path.basename(target_find)
            ori_mask_path = os.path.join(match_mask, target_mask_name)
            target_save_name = name.split('.')[0] + '_mask.tif'
            shutil.copy(ori_mask_path, os.path.join(out_match_ori, target_save_name))

        print(name)



if __name__ == '__main__':
    main()

