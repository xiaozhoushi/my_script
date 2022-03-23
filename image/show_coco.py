import os
from pycocotools.coco import COCO
from skimage import io
from matplotlib import pyplot as plt

json_file = '/User/bytedance/Documents/data/colonoscopy_images/segmentation/instance_seg_t1_crop.json'
dataset_dir = ''
coco = COCO(json_file)
catIds = coco.getCatIds(catNms='lesion')
imgIds = coco.getImgIds(catIds=catIds)
for i in range(10):
    img = coco.loadImgs(imgIds[i])[0]
    I = io.imread(dataset_dir + img['file_name'])
    plt.axis('off')
    plt.imshow(I) 
    annIds = coco.getAnnIds(imgIds=img['id'], catIds=catIds, iscrowd=None)
    anns = coco.loadAnns(annIds)
    coco.showAnns(anns)
    plt.show()
