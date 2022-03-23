import os
from multiprocessing import Pool
from PIL import Image
from pycocotools.coco import COCO
import numpy as np


def get_img_mask(i, coco, save_path, mask_save_path):
    imgInfo = coco.loadImgs(i)[0]
    url, id = imgInfo['imagex_url'], imgInfo['id']
    crop = imgInfo['crop']
    height, width = imgInfo['height'], imgInfo['width']
    name = os.path.join(save_path, str(id).zfill(5) + '.jpg')
    commend = 'wget ' + url + ' -O ' + name
    os.system(commend)
    img = Image.open(name)
    if crop[2] - crop[0] != width or crop[3] - crop[1] != height:
        print('error')
        return
    img = img.crop((crop[0], crop[1], crop[2], crop[3]))
    img.save(name)
    
    annIds = coco.getAnnIds(imgIds = id)
    anns = coco.loadAnns(annIds)
    mask = np.zeros((height, width))
    for single in anns:
        single_mask = coco.annToMask(single)
        mask += single_mask
    mask[mask > 0] = 255
    mask = Image.fromarray(np.uint8(mask))
    mask_name = os.path.join(mask_save_path, str(id).zfill(5) + '_mask.jpg')
    mask.save(mask_name)
    print('process:', name)



def main():
    json_path = '/Users/bytedance/Documents/data/colonoscopy_images/segmentation/instance_seg_t1_crop_new.json'
    save_path = '/Users/bytedance/Documents/data/colonoscopy_images/segmentation/'
    img_save_path = os.path.join(save_path, 'img_file')
    if not os.path.exists(img_save_path):
        os.mkdir(img_save_path)
    mask_save_path = os.path.join(save_path, 'mask_file')
    if not os.path.exists(mask_save_path):
        os.mkdir(mask_save_path)
    coco = COCO(json_path)
    catIds = coco.getCatIds(catNms=['lesion'])
    imgIds = coco.getImgIds(catIds = catIds)
    print('image nums:', len(imgIds))
    pool = Pool(processes=6)
    for i in range(len(imgIds)):
        pool.apply_async(get_img_mask, [i, coco, img_save_path, mask_save_path])
        # get_img_mask(i, coco, img_save_path, mask_save_path)
    pool.close()
    pool.join()


if __name__ == '__main__':
    main()
