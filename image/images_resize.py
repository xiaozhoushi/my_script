import os
from PIL import Image
from multiprocessing import Pool


def resize(image_path, save_path):
    image = Image.open(image_path)
    width, height = image.size
    #image = image.resize((width//4, height//4))
    image = image.resize((512, 512))
    image_name = os.path.basename(image_path)
    image.save(os.path.join(save_path, image_name))
    print('processing:', image_path)

def main():
    input_path = '/Users/Documents/data/colonoscopy_images/seg_resize_512/img_file_test'
    save_path = '/Users/Documents/data/colonoscopy_images/seg_resize_512/img_file_test'
    image_list = [os.path.join(input_path, item) for item in os.listdir(input_path) if '.jpg' in item]
    pool = Pool(processes=6)
    for img_path in image_list:
        pool.apply_async(resize, [img_path, save_path])
    pool.close()
    pool.join()

if __name__ == '__main__':
    main()
    
