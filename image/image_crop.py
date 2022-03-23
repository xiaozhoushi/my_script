from PIL import Image
import os

def main():
    '''
    按照区域裁剪图像
    '''
    input_path = '/Users/Documents/data/colonoscopy_images/02_src'
    save_path = '/Users/Documents/data/colonoscopy_images/02'
    img_list = os.listdir(input_path)
    for img_name in img_list:
        if '.jpg' in img_name:
            img_path = os.path.join(input_path, img_name)
            img = Image.open(img_path)
            img = img.crop((280, 92, 678, 460)) #left, up, right, down
            img.save(os.path.join(save_path, img_name))
            print('save:', img_name)

if __name__ == '__main__':
    main()
