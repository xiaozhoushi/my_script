import os
import numpy as np
import matplotlib.pyplot as plt
import random

def main():
    path = '/Users/bytedance/Documents/data/public_data/kvasir/images'
    out_path = '/Users/bytedance/Downloads/res.png'
    data_list = []
    for img_root, _, img_names in os.walk(path):
        data_tmp = [os.path.join(img_root, name) for name in img_names if is_image_file(name)]
        data_list += data_tmp
    n_total = len(data_list)
    print('image number:', n_total)
    
    height, width = [], []
    for item in data_list:
        img = plt.imread(item)
        shape = img.shape
        height.append(shape[0])
        width.append(shape[1])
    kwargs = dict(histtype = 'stepfilled', alpha = 0.5, bins = 30)
    plt.hist(height, label = 'height', **kwargs)
    plt.hist(width, label = 'width', **kwargs)
    plt.legend(loc = 'upper left')
    plt.savefig(out_path)
    plt.show()


def is_image_file(filename):
    return any(filename.endswith(extension) for extension in ['.png', '.jpg', '.tif', '.jpeg', '.PNG', '.JPG', '.JPEG', '.bmp', '.BMP'])

if __name__ == '__main__':
    main()
