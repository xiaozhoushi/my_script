# coding: utf-8
import cv2
import os
import sys
import numpy as np

from multiprocessing import Pool

#from class_model.forward import Is_clear


def is_video(filename):
    return any(filename.endswith(extension) for extension in ['.avi', '.mp4'])

#def longest_subarray(array):
#    res = 0
#    pre = -1
#    for i in range(len(array)):
#        if array[i] > 20:
#            if pre == -1:
#                pre = i
#            count = i - pre + 1
#            res = max(res, count)
#        else:
#            pre = -1
#    return res
#
#def crop(img):
#    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#    h, w = gray_img.shape
#    xs = np.zeros((w))
#    for i in range(w):
#        xs[i] = longest_subarray(gray_img[:, i])
#    ys = np.zeros((h))
#    for i in range(h):
#        ys[i] = longest_subarray(gray_img[i, :])
#    ratio = 0.3
#    x1, x2 = None, None
#    for i in range(w):
#        if xs[i] > h * ratio:
#            x1 = i
#            break
#    for i in range(w - 1, -1, -1):
#        if xs[i] > h * ratio:
#            x2 = i
#            break
#    y1, y2 = None, None
#    for i in range(h):
#        if ys[i] > w * ratio:
#            y1 = i
#            break
#    for i in range(h - 1, -1, -1):
#        if ys[i] > w * ratio:
#            y2 = i
#            break
#    if x1 == None or x2 == None or y1 == None or y2 == None or x1 >= x2 or y1 >= y2:
#        crop = img
#    else:
#        crop = img[y1: y2, x1: x2]
#    return crop


class Draw_frame:
    '''
    draw_frame
    '''
    def __init__(self, save_path):
        self.save_path = save_path
        #self.is_clear = Is_clear()
    
    def get_frame(self, video_file):
        video_name = os.path.basename(video_file.split('.')[0])
        image_save_path = os.path.join(self.save_path, video_name)
        if not os.path.exists(image_save_path):
            os.makedirs(image_save_path)
        vc = cv2.VideoCapture(video_file)
        fps = vc.get(cv2.CAP_PROP_FPS)
        num_frames = vc.get(cv2.CAP_PROP_FRAME_COUNT)
        save_info = str(num_frames) + '_' + str('%.2f'%fps)
        success, frame = vc.read()
        i = 0
        while success:
            #frame = crop(frame)
            #if self.is_clear.forward(frame):
            if i % 7 == 0:
                save_image(frame, image_save_path, i, video_name, save_info)
                print('save image:',i)
            i += 1
            success, frame = vc.read()
        vc.release()


def save_image(image, addr, num, video_name, save_info):
    address = os.path.join(addr, str(num).zfill(5)+'.jpg')
    cv2.imwrite(address, image)


def main():
    video_path = '/Users/bytedance/Documents/Documents/data/colonoscopy_video'
    save_path = '/Users/bytedance/Documents/Documents/data/colonoscopy_video'
    pool = Pool(processes=6)
    draw_frame = Draw_frame(save_path)
    video_files = []
    for video_root, _, video_names in os.walk(video_path):
        video_files += [os.path.join(video_root, name) for name in video_names if '._' not in name and is_video(name)]
    for video_file in video_files:
        print(video_file)
        pool.apply_async(draw_frame.get_frame, [video_file])

    pool.close()
    pool.join()

def main_1():
    video_path = '/Users/bytedance/Documents/data/sample/video/lotus_endo.mp4'
    save_path = '/Users/bytedance/Documents/data/sample/image'

    draw_frame = Draw_frame(save_path)
    draw_frame.get_frame(video_path)
    


if __name__ == '__main__':
    main_1()
