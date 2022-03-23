from PIL import Image
import numpy as np
import os
from multiprocessing import Pool
import glob


def tif2bmp(img_path, out_dir):
    img = Image.open(img_path).convert('L')

    img_name = os.path.basename(img_path)
    new_name = img_name.split('_')[0]+'.bmp'
    new_path = os.path.join(out_dir, new_name)
    
    img.save(new_path, format='BMP')
    print('processe:', img_name)


def main():
    input_dir = '/Users/bytedance/Documents/data/GIANA_challenge/segmentation/SegmentationTrainingUpload'
    out_dir = '/Users/bytedance/Documents/data/GIANA_challenge/segmentation/SegmentationTrainingUpload/masks'

    all_img = glob.glob(input_dir + '/*.tif')
    pool = Pool(processes=6)
    print('image lenght:', len(all_img))
    for img_path in all_img:
        pool.apply_async(tif2bmp, [img_path, out_dir])
    pool.close()
    pool.join()


if __name__ == '__main__':
    main()

    
