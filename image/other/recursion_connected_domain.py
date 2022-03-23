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
sys.setrecursionlimit(10000000)


def recursive_seed(binary_img: np.array, seed_row, seed_col, offsets, num):
    rows, cols = binary_img.shape
    var = binary_img[seed_row][seed_col]
    if var != 1:
        return
    binary_img[seed_row][seed_col] = num
    for offset in offsets:
        neighbor_row = min(max(0, seed_row+offset[0]), rows-1)
        neighbor_col = min(max(0, seed_col+offset[1]), cols-1)
        recursive_seed(binary_img, neighbor_row, neighbor_col, offsets, num)


def Seed_Filling(binary_img, neighbor_hoods, area_num = 2, max_num=100):
    if neighbor_hoods == NEIGHBOR_HOODS_4:
        offsets = OFFSETS_4
    elif neighbor_hoods == NEIGHBOR_HOODS_8:
        offsets = OFFSETS_8
    else:
        raise ValueError

    rows, cols = binary_img.shape
    for row in range(rows):
        for col in range(cols):
            var = binary_img[row][col]
            if var == 1 and area_num <= max_num:
                recursive_seed(binary_img, row, col, offsets, area_num)
                area_num += 1


def area(img, star_num):
    max_num = img.max()
    area_list = [0] * (max_num + 1)
    raws, cols = img.shape
    for i in range(raws):
        for j in range(cols):
            var = img[i][j]
            area_list[var] += 1

    if len(area_list) > 1:
        max_area = max(area_list[1:])
        max_area_num = area_list.index(max_area)
        img[img != max_area_num] = 0
        img[img == max_area_num] = 255


def main():
    input_path = '/Users/Documents/data/test_tmp/result'
    out_path = '/Users/Documents/data/test_tmp/result'
    max_num, star_num = 1000, 2
    img_list = glob.glob(input_path+'/*.jpg')
    print(len(img_list))
    for img_path in img_list:
        img = Image.open(img_path)
        img = np.array(img)
        img[img>125] = 255
        img[img<=125] = 0
        img = (img / 255).astype(np.uint8)
        
        Seed_Filling(img, NEIGHBOR_HOODS_8, star_num, max_num)

        area(img, star_num)

        img = Image.fromarray(img.astype(np.uint8))
        name = os.path.basename(img_path).split('.')[0] + '_area.jpg'
        img_save_path = os.path.join(out_path,name)
        img.save(img_save_path)
        print(img_save_path)


if __name__ == "__main__":
    main()
    
