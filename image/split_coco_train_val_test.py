import os
from pycocotools.coco import COCO
import shutil
import json

def main():
    json_file = '/Users/bytedance/Documents/data/colonoscopy_images/detection_segmentation/T1_seg_crop.json'
    dataset_dir = '/Users/bytedance/Documents/data/colonoscopy_images/detection_segmentation/all_new'
    out_dir = '/Users/bytedance/Documents/data/colonoscopy_images/detection_segmentation/split_T1_crop'
    with open(json_file, 'r', encoding='UTF-8') as f:
        dict_data = json.load(f)
    images = dict_data['images']
    annotations = dict_data['annotations']
    train_images, test_images = [], []
    train_anno, test_anno = [], []
    val_images, val_anno = [], []
    split_len_train, split_len_val = len(images) * 4 // 5, len(images) * 9 // 10
    train_dir = os.path.join(out_dir, 'train')
    val_dir = os.path.join(out_dir, 'val')
    test_dir = os.path.join(out_dir, 'test')
    if not os.path.exists(train_dir):
        os.makedirs(train_dir)
    if not os.path.exists(val_dir):
        os.makedirs(val_dir)
    if not os.path.exists(test_dir):
        os.makedirs(test_dir)
    for i in range(len(images)):
        tmp = images[i]['file_name']
        name = str(i).zfill(5) + '.jpg'
        images[i]['file_name'] = name
        if i < split_len_train:
            shutil.move(os.path.join(dataset_dir, tmp), os.path.join(train_dir,name))
            train_images.append(images[i])
            while len(annotations) > 0 and annotations[0]['image_id'] == images[i]['id']:
                    train_anno.append(annotations[0])
                    annotations.pop(0)
        elif i < split_len_val:
            shutil.move(os.path.join(dataset_dir, tmp), os.path.join(val_dir,name))
            val_images.append(images[i])
            while len(annotations) > 0 and annotations[0]['image_id'] == images[i]['id']:
                    val_anno.append(annotations[0])
                    annotations.pop(0)
        else:
            shutil.move(os.path.join(dataset_dir, tmp), os.path.join(test_dir,name))
            test_images.append(images[i])
            while len(annotations) > 0 and annotations[0]['image_id'] == images[i]['id']:
                    test_anno.append(annotations[0])
                    annotations.pop(0)
    train_dict = {
        'info':dict_data['info'],
        'categories': dict_data['categories'],
        'images' : train_images,
        'annotations' : train_anno
    }
    val_dict = {
        'info':dict_data['info'],
        'categories': dict_data['categories'],
        'images' : val_images,
        'annotations' : val_anno
    }
    test_dict = {
        'info':dict_data['info'],
        'categories': dict_data['categories'],
        'images' : test_images,
        'annotations' : test_anno
    }
    with open(os.path.join(out_dir, 'polyps_det_train.json'), 'w', encoding = 'UTF-8') as f:
        json.dump(train_dict, f)
    with open(os.path.join(out_dir, 'polyps_det_val.json'), 'w', encoding = 'UTF-8') as f:
        json.dump(val_dict, f)
    with open(os.path.join(out_dir, 'polyps_det_test.json'), 'w', encoding = 'UTF-8') as f:
        json.dump(test_dict, f)
    print('Done')

    
if __name__ == '__main__':
    main()

