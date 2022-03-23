# coding:utf-8

from __future__ import print_function
from ttvcloud.imagex.ImageXService import ImageXService
import os
import datetime 

def isImage(name):
    image_type = ['jpg', 'png', 'JPG', 'jpeg', ' PNG']
    return True if name.split('.')[-1] in image_type else False

if __name__ == '__main__':
    imagex_service = ImageXService()

    # call below method if you dont set ak and sk in $HOME/.vcloud/config
    imagex_service.set_ak('')
    imagex_service.set_sk('')
    service_id = ''

    step = 5
    out_path = '/Users/bytedance/Documents/Documents/data/imageX_url/images_test.txt'
    img_path = '/Users/bytedance/Documents/Documents/data/colonoscopy_images/images'
    img_files = []
    for img_root, _, img_names in os.walk(img_path):
        img_files += [os.path.join(img_root, name) for name in img_names if isImage(name)]

    #for i in range(0, len(img_files), step):
    for i in range(0, 2000, step): ##############
        print('step :', i)
        #end = min(i+step, len(file_paths))
        end = min(i+step, 2000) ##############
        tmp = img_files[i:end]
        resp = imagex_service.upload_image(service_id, tmp)
        with open(out_path, 'a') as f:
            for j in range(len(tmp)):
                res = imagex_service.get_image_info(service_id, resp['Results'][j]['Uri'])
                data = res['FileName'] + ' ' + res['ImageURL'] + ' ' + tmp[j] + '\n'
                f.write(data)
        
