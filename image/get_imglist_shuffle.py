import os
import random

def isImage(name):
    image_type = ['jpg', 'png', 'JPG', 'jpeg', ' PNG']
    return True if name.split('.')[-1] in image_type else False

def main():
    '''
    获取文件夹下所有图像路径
    '''
    input_path = '/home/tiger/video_data/20201220_images'
    out_path = '/home/tiger/video_data/20201220_imglist.txt'
    img_list = []
    for img_root, _, names in os.walk(input_path):
        tmp = [os.path.join(img_root, name) for name in names if isImage(name)]
        img_list += tmp
    random.shuffle(img_list)
    with open(out_path, 'w') as f:
        for name in img_list:
            if isImage(name):
                f.write(str(os.path.join(input_path, name + '\n')))
    print('ok')

if __name__ == '__main__':
    main()