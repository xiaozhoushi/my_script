from PIL import Image
import numpy as np
import cv2

path = '/Users/bytedance/Documents/data/GiANA_challenge/segmentation/train/cvc300/masks/1.bmp'
res = [0] * 256
#img = Image.open(path, 'r').convert('L')
#w,h = img.size
#arr = np.array(img)
img = cv2.imread(path, 0)
h, w = img.shape
start_w, end_w = w // 2 - 10, w//2+10
start_h, end_h = h //2-10, h//2+10
arr = img[start_h:end_h, start_w:end_w]
print(res)
for r in range(h):
    for c in range(w):
        res[img[r, c]] += 1
print(res)
