import os
import shutil
from multiprocessing import Pool 

############
#for colmap#
############
def get_image_by_url_file(save_path, url_dir, url_file):
    save_img_path = os.path.join(save_path, url_file.split('.')[0])
    if not os.path.exists(save_img_path):
        os.mkdir(save_img_path)
    url_file_path = os.path.join(url_dir, url_file)
    before_id, range_frame = 0, 1
    with open(url_file_path, 'r') as f:
        url_data = f.readlines()
        for i in range(len(url_data)):
            id_str, url = url_data[i].split()
            id_now = int(id_str)
            if id_now - before_id >= range_frame:
                img_name = id_str.zfill(5)
                img_path = os.path.join(save_img_path, img_name + '.jpg')
                commend = 'wget ' + url + ' -O ' + img_path
                os.system(commend)
                before_id = id_now


if __name__ == '__main__':
    url_dir = '/Users/bytedance/Documents/data/imageX_url/data'
    save_path = '/Users/bytedance/Documents/data/colonoscopy_images/04'
    url_files = os.listdir(url_dir)
    url_files.remove('video_url.txt')
    pool = Pool(processes=6)
    for i, url_file in enumerate(url_files):
        if i < 1:
            print(url_file)
            pool.apply_async(get_image_by_url_file, [save_path, url_dir, url_file])
    pool.close()
    pool.join()