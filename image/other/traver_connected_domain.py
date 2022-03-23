import numpy as np
from PIL import Image
import glob
import os
import sys

# 4邻域的连通域和 8邻域的连通域
# [row, col]
NEIGHBOR_HOODS_4 = True
OFFSETS_4 = [[0, -1], [-1, 0], [0, 0], [1, 0], [0, 1]]

NEIGHBOR_HOODS_8 = False
OFFSETS_8 = [[-1, -1], [0, -1], [1, -1],
             [-1,  0], [0,  0], [1,  0],
             [-1,  1], [0,  1], [1,  1]]

def neighbor_value(img: np.array, offsets, reverse=False):
    rows, cols = img.shape
    label_idx = 0
    rows_ = [0, rows, 1] if reverse == False else [rows-1, -1, -1]
    cols_ = [0, cols, 1] if reverse == False else [cols-1, -2, -1]
    for row in range(rows_[0], rows_[1], rows_[2]):
        for col in range(cols_[0], cols_[1], cols_[2]):
            label = 256
            if img[row][col] < 125:
                continue
            for offset in offsets:
                neighbor_row = min(max(0, row+offset[0]), rows-1)
                neighbor_col = min(max(0, col+offset[1]), cols-1)
                neighbor_val = img[neighbor_row, neighbor_col]
                if neighbor_val == 0:
                    continue
                label = neighbor_val if neighbor_val < label else label
            if label == 255:
                label_idx += 1
                label = label_idx
            img[row][col] = label


def traverse(img: np.array, neighbor_hoods):
    if neighbor_hoods == NEIGHBOR_HOODS_4:
        offsets = OFFSETS_4
    else:
        offsets = OFFSETS_8

    neighbor_value(img, offsets)

def area(img):
    max_num = img.max()
    area_list = [0] * (max_num + 1)
    raws, cols = img.shape
    for i in range(raws):
        for j in range(cols):
            var = img[i][j]
            area_list[var] += 1
    print(area_list)

    if len(area_list) > 1:
        max_area = max(area_list[1:])
        max_area_num = area_list.index(max_area)
        img[img != max_area_num] = 0
        img[img == max_area_num] = 255


def main():
    input_path = '/Users/Documents/data/test_tmp/result'
    out_path = '/Users/Documents/data/test_tmp/result'
    img_list = glob.glob(input_path+'/*.jpg')
    print(len(img_list))
    for img_path in img_list:
        img = Image.open(img_path)
        img = np.array(img)
        img[img>125] = 255
        img[img<=125] = 0
        
        traverse(img, NEIGHBOR_HOODS_8)

        area(img)

        img = Image.fromarray(img.astype(np.uint8))
        name = os.path.basename(img_path).split('.')[0] + '_area.jpg'
        img_save_path = os.path.join(out_path,name)
        img.save(img_save_path)
        print(img_save_path)
        break


if __name__ == "__main__":
    main()
    
