import numpy as np
from PIL import Image
import glob
import os
import sys
import skimage.measure as measure



def main():
    input_path = '/Users/Documents/data/test_tmp/result'
    out_path = '/Users/Documents/data/test_tmp/result'
    max_num, star_num = 1000, 2
    img_list = glob.glob(input_path+'/*.jpg')
    print(len(img_list))
    for img_path in img_list:
        img = Image.open(img_path).convert('L')
        img = np.array(img).astype(np.uint8)
        img[img>125] = 255 
        img[img<=125] = 0

        #label_img, num = measure.label(img, neighbors=8,background=0,return_num = True)
        label_img = measure.label(img, connectivity=2)
        max_label, max_area = 0, 0
        properties = measure.regionprops(label_img)
        for prop in properties:
            if prop.area > max_area:
                max_label = prop.label
                max_area = prop.area
        if max_label != 0:
            img[label_img == max_label] = 255
            img[label_img != max_label] = 0

        img = Image.fromarray(img.astype(np.uint8))
        name = os.path.basename(img_path).split('.')[0] + '_area.jpg'
        img_save_path = os.path.join(out_path,name)
        img.save(img_save_path)
        print(img_save_path)


if __name__ == "__main__":
    main()
    
