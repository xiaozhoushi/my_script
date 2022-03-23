import os
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import random

def main():
    path = '/Users/bytedance/Documents/Documents/data/images/classfication/class_train/1'
    out_path = '/Users/bytedance/Downloads/res.png'
    row, clom = 3, 5
    data_list = []
    for img_root, _, img_names in os.walk(path):
        data_tmp = [os.path.join(img_root, name) for name in img_names if is_image_file(name)]
        data_list += data_tmp
    n_total = len(data_list)
    print('image number:', n_total)
    random.shuffle(data_list)
    
    plt.figure()
    plt.suptitle('mutil image')
    for index in range(row*clom):
        img = Image.open(data_list[index])
        name = os.path.basename(data_list[index])
        plt.subplot(row, clom, index + 1)
        plt.title('label 1')
        plt.imshow(img)
        plt.axis('on')
    plt.savefig(out_path)
    plt.show()


def is_image_file(filename):
    return any(filename.endswith(extension) for extension in ['.png', '.jpg', '.jpeg', '.PNG', '.JPG', '.JPEG'])

if __name__ == '__main__':
    main()