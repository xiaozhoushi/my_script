import os

def isImage(name):
    image_type = ['jpg', 'png', 'JPG', 'jpeg', ' PNG']
    return True if name.split('.')[-1] in image_type else False

def main():
    '''
    获取文件夹下所有图像路径
    '''
    input_path = '/Users/Documents/data/colonoscopy_images/01'
    out_path = '/Users/Documents/data/colonoscopy_images/train_01.txt'
    img_list = sorted(os.listdir(input_path))
    with open(out_path, 'w') as f:
        for name in img_list:
            if isImage(name):
                f.write(str(os.path.join(input_path, name + '\n')))
    print('ok')

if __name__ == '__main__':
    main()
