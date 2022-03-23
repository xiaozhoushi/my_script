import os
import shutil


def main():
    input_path = '/Users/bytedance/Documents/data/classfication/archive/images/Images'
    output_path = '/Users/bytedance/Documents/data/classfication/archive/images/val'
    dir_list = [x for x in os.listdir(input_path) if 'n02' in x]
    print(len(dir_list))
    for dir in dir_list:
        input_dir = os.path.join(input_path, dir)
        output_dir = os.path.join(output_path, dir)
        img_list = [x for x in os.listdir(input_dir) if '.jpg' in x]
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        for index in range(len(img_list) // 10):
            img_input_path = os.path.join(input_dir, img_list[index])
            img_output_path = os.path.join(output_dir, img_list[index])
            shutil.move(img_input_path, img_output_path)
        print(dir)


if __name__ == '__main__':
    main()
