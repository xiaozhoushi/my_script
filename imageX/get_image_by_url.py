import os
import csv
import shutil
from multiprocessing import Pool 



def img_down(i, item, train_data_path):
    if i == 0:
        return
    label = item[4] if item[4] != '' else item[2]
    img_path = os.path.join(train_data_path, label)
    if not os.path.exists(img_path):
        os.mkdir(img_path)
    name = item[0] +'.jpg'
    commend = 'wget ' + item[1] + ' -O ' + os.path.join(img_path, name)
    os.system(commend)



if __name__ == '__main__':
    csv_path = '/Users/bytedance/Downloads/48549139123027269.csv'
    train_data_path = '/Users/bytedance/Documents/Documents/data/images/04'
    pool = Pool(processes=6)
    with open(csv_path, 'r') as f:
        csv_data = csv.reader(f)
        for i, item in enumerate(csv_data):
            pool.apply_async(img_down, [i, item, train_data_path])
    pool.close()
    pool.join()