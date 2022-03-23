# coding:utf-8

from __future__ import print_function
from ttvcloud.imagex.ImageXService import ImageXService
import os
import datetime
from multiprocessing import Pool 

def isImage(name):
    image_type = ['jpg', 'png', 'JPG', 'jpeg', ' PNG']
    return True if name.split('.')[-1] in image_type else False


def upload(i, step, img_files, imagex_service, out_path):
    print('step :', i)
    #end = min(i+step, len(file_paths))
    end = min(i+step, 30000) ##############
    tmp = img_files[i:end]
    resp = imagex_service.upload_image(service_id, tmp)
    with open(out_path, 'a') as f:
        for j in range(len(tmp)):
            res = imagex_service.get_image_info(service_id, resp['Results'][j]['Uri'])
            data = res['FileName'] + ' ' + res['ImageURL'] + ' ' + tmp[j] + '\n'
            f.write(data)

if __name__ == '__main__':
    imagex_service = ImageXService()

    # call below method if you dont set ak and sk in $HOME/.vcloud/config
    imagex_service.set_ak('')
    imagex_service.set_sk('')
    service_id = ''

    step = 5
    out_path = '/home/tiger/video_data/txt/20201220_imageX_30000.txt'
    img_path = '/home/tiger/video_data/txt/20201220_imglist.txt'
    img_files = []
    with open(img_path, 'r') as f:
        img_files = [item.strip('\n') for item in f.readlines()]
    pool = Pool(processes=6)
    #for i in range(0, len(img_files), step):
    for i in range(12890, 30000, step): ##############
        pool.apply_async(upload, [i, step, img_files, imagex_service, out_path])
    pool.close()
    pool.join()
        
