import shutil
import os
import glob
from multiprocessing import Pool


def move_image(img_path, out_dir):
    shutil.move(img_path, out_dir)

def main():
    input_dir = '/Users/bytedance/Documents/data/GIANA_challenge/segmentation/SegmentationTrainingUpload'
    out_dir = '/Users/bytedance/Documents/data/GIANA_challenge/segmentation/SegmentationTrainingUpload/images'
    all_img = glob.glob(input_dir + '/*.bmp')
    pool = Pool(processes=6)
    for img_path in all_img:
        pool.apply_async(move_image, [img_path, out_dir])
    pool.close()
    pool.join()


if __name__ == '__main__':
    main()
