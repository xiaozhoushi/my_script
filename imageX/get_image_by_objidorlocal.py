# -*- coding: utf-8 -*- 
import os
import csv
import shutil


csv_path = '/Users/bytedance/Downloads/168419304_LwtQbAPA2Ld7TzLR_gbk.csv'
image_url_path = '/Users/bytedance/Documents/Documents/data/imageX_url/20201214_1.txt'
train_data_path = '/Users/bytedance/Documents/Documents/data/images/04'
use_local = True

img_obj_url = []
with open(csv_path, 'r') as f:
    csv_data = csv.reader(f)
    with open(image_url_path, 'r') as f_url:
        img_obj_url = [tmp.strip('\n').split() for tmp in f_url.readlines()]
        for i, item in enumerate(csv_data):
            # if i == 0:
            #     continue
            img_path = os.path.join(train_data_path, item[2])
            if not os.path.exists(img_path):
                os.mkdir(img_path)
            for img_infor in img_obj_url:
                if item[0] == img_infor[0]:
                    if use_local:
                        name = os.path.basename(img_infor[3])
                        print(name)
                        shutil.copy(img_infor[3], os.path.join(img_path, name))
                    else:
                        name = item[0] +'.jpg'
                        commend = 'wget ' + img_infor[2] + ' -O ' + os.path.join(img_path, name)
                        os.system(commend)
            