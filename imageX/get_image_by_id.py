import os
import csv
import shutil
from multiprocessing import Pool 

######################
#根据图像的id从imageX上下载图像
######################

def img_down(item, data_path):
    url = '-i-vfhc8amni0/' + item + '~tplv-vfhc8amni0-image.image'
    commend = 'wget ' + url + ' -O ' + os.path.join(data_path, item)
    os.system(commend)



if __name__ == '__main__':
    csv_path = '/Users/bytedance/Documents/data/nbi_id/abandon_0713.txt'
    data_path = '/Users/bytedance/Documents/data/nbi_images'
    if not os.path.exists(data_path):
        os.mkdir(data_path)
    pool = Pool(processes=6)
    with open(csv_path, 'r') as f:
        csv_data = f.readlines()
        for i, item in enumerate(csv_data):
            item = item.strip('\n')
            pool.apply_async(img_down, [item, data_path])
    pool.close()
    pool.join()
