from PIL import Image
import numpy as np
import os
from multiprocessing import Pool
import glob
import tifffile as tif
import cv2

# tif具有隐藏的不同格式，有的可以使用tifffile读取转换成npg，有的可以使用cv2读取转换成png。

def tif2png(img_path, out_dir):
    #img = Image.open(img_path).convert('L')
    #img = Image.open(img_path).convert('RGB')
    img = cv2.imread(img_path)
    #img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #img = tif.imread(img_path)
    img = Image.fromarray(img.astype(np.uint8))
    #img.show()
    #img =img.convert('L')

    img_name = os.path.basename(img_path)
    new_name = img_name.split('.')[0]+'.png'
    new_path = os.path.join(out_dir, new_name)
    
    img.save(new_path, format='png')
    print('processe:', img_name)


def main():
    input_dir = '/Users/bytedance/Documents/data/public_data/ETIS-LaribPolypDB/Ground Truth'
    out_dir = '/Users/bytedance/Documents/data/public_data/ETIS/masks'

    all_img = glob.glob(input_dir + '/*.tif')
    pool = Pool(processes=6)
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)
    print('image lenght:', len(all_img))
    for img_path in all_img:
        #tif2png(img_path, out_dir)
        pool.apply_async(tif2png, [img_path, out_dir])
    pool.close()
    pool.join()


if __name__ == '__main__':
    main()

    
