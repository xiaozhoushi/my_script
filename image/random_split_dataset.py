import os
import glob
import random
import shutil


def is_image_file(filename):
    return any(filename.endswith(extension) for extension in ['.png', '.jpg', '.jpeg', '.PNG', '.JPG', '.JPEG'])


def main():
    input_path = '/Users/bytedance/Documents/data/colonoscopy_images/segmentation'
    ratio = 0.8
    shuffle = True

    img_path = os.path.join(input_path, 'img_file')
    mask_path = os.path.join(input_path, 'mask_file')

    img_out_path = os.path.join(input_path, 'img_file_test')
    mask_out_path = os.path.join(input_path, 'mask_file_test')

    if not os.path.exists(img_out_path):
        os.mkdir(img_out_path)

    if not os.path.exists(mask_out_path):
        os.mkdir(mask_out_path)
    
    img_list = [ name for name in glob.glob(img_path + '/*.jpg') if is_image_file(name)]
    n_total = len(img_list)
    offset = int(n_total * ratio)
    if shuffle:
        random.shuffle(img_list)
    train_list = img_list[:offset]
    test_list = img_list[offset:]
    print('train lenght:', len(train_list))
    print('test lenght:', len(test_list))
    
    for item in test_list:
        name = os.path.basename(item)
        shutil.move(item, os.path.join(img_out_path, name))

        mask_name = name.split('.')[0] + '_mask.jpg'
        item_mask = os.path.join(mask_path, mask_name)
        if os.path.exists(item_mask):
            shutil.move(item_mask, os.path.join(mask_out_path, mask_name))
        print('processes: ', name)


if __name__ == "__main__":
    main()
