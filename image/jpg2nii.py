from PIL import Image
import numpy as np
import os
from multiprocessing import Pool
import glob
import SimpleITK as sitk
import math



def main():
    input_path = '/Users/bytedance/Documents/data/test_tmp'
    out_path = '/Users/bytedance/Documents/data/test_tmp1'
    pre_num = 50

    all_file = [name for name in glob.glob(input_path + '/*.jpg')]
    all_file.sorted()
    print('all image name:', len(all_file))

    for num in range(math.ceil(len(all_file) / pre_num))
        if num != math.ceil(len(all_file) / pre_num) - 1:
            stack_num = pre_num
        else:
            stack_num = len(all_file) % pre_num
        all_img = np.zeros([256, 256, stack_num]) 
        for i in range(stack_num):
            index = num * pre_num + i 
            img = Image.open(all_file[index]) 
            img = img.convert('L')
            img = np.asarray(img)
            all_img[i] = img
        all_img = sitk.ReadImage(all_img)
        save_path = os.path.join(out_path, ' result_' + str(num) + '.nii')
        sitk.WriteImage(all_img, save_path)
