import os
import numpy as np
from PIL import Image
import random
import glob

def main():
    path = '/Users/bytedance/Documents/data/test_tmp/result'
    out_path = '/Users/bytedance/Documents/data/test_tmp/tmp'
    data_list = [item for item in glob.glob(path + '/*.png') if 'mask' not in item]
    n_total = len(data_list)
    print('image number:', n_total)
    for img_path in data_list:
        name = os.path.basename(img_path)
        img = Image.open(img_path)
        mask = Image.open(os.path.join(path, name.split('.')[0]+'_mask.png'))
        pred = Image.open(os.path.join(path, name.split('.')[0] + '_pred.jpg'))
        img, mask, pred = np.array(img), np.array(mask), np.array(pred)
        mask[mask > 125] = 255
        mask[mask <=125] = 0
        pred[pred > 125] = 255 
        pred[pred <= 125] = 0
        h, w = mask.shape
        for row in range(h):
            for col in range(w):
                if mask[row, col] == 255 and pred[row,col] == 255:
                    img[row, col, 0] = 255
                elif mask[row, col] == 255 and pred[row, col] == 0:
                    img[row, col, 1] = 255
                elif mask[row,col] == 0 and pred[row, col] == 255:
                    img[row, col, 2] = 255
        img = Image.fromarray(img.astype(np.uint8))
        img.save(os.path.join(out_path, name))
        print(name)



def is_image_file(filename):
    return any(filename.endswith(extension) for extension in ['.png', '.jpg', '.jpeg', '.PNG', '.JPG', '.JPEG'])

if __name__ == '__main__':
    main()
