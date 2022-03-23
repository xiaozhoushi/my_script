import argparse
import copy
import os
from PIL import Image
import numpy as np
import glob 
import cv2

import skimage.measure as measure


def parse_args():
    parser = argparse.ArgumentParser(description='test Super Resolution Models')
    # data
    parser.add_argument('--pred_path', default = '/Users/Documents/data/test_tmp/', type = str, help = ' val image path')
    parser.add_argument('--gt_path', default = '/Users/Documents/data/GIANA_challenge/segmentation/test_match/cvc612/mask', type = str)
    parser.add_argument('--label_path', default = '/mnt/bd/aurora-mtrc-data', type = str)
    #test 
    parser.add_argument('--threshold', default = 0.5, type = int)
    parser.add_argument('--connected_domain', default = False, type = bool)
    # model
    parser.add_argument('--num_classes', default =2, type = int, help = 'number of classes')

    args = parser.parse_args()
    return args



class IOUMetric:
    """
    Class to calculate mean-iou using fast_hist method
    """
    def __init__(self, num_classes, threshold = None):
        self.threshold = threshold
        self.num_classes = num_classes
        self.hist = np.zeros((num_classes, num_classes))
    def _fast_hist(self, label_pred, label_true):
        mask = (label_true >= 0) & (label_true < self.num_classes)
        hist = np.bincount(
            self.num_classes * label_true[mask].astype(int) +
            label_pred[mask], minlength=self.num_classes ** 2).reshape(self.num_classes, self.num_classes)
        return hist
    def add_batch(self, predictions, gts ):
        predictions, gts = np.array(predictions), np.array(gts)
        predictions[predictions >= self.threshold] = 1
        predictions[predictions < self.threshold] = 0
        gts[gts >=125] = 255
        gts[gts < 125] = 0
        gts[gts==255] = 1
        predictions = predictions.astype(np.uint8)
        gts = gts.astype(np.uint8)
        for lp, lt in zip(predictions, gts):
            self.hist += self._fast_hist(lp.flatten(), lt.flatten())
    def evaluate(self):
        acc = np.diag(self.hist).sum() / self.hist.sum()
        acc_cls = np.diag(self.hist) / self.hist.sum(axis=1)
        acc_cls = np.nanmean(acc_cls)
        iu = np.diag(self.hist) / (self.hist.sum(axis=1) + self.hist.sum(axis=0) - np.diag(self.hist))
        mean_iu = np.nanmean(iu)
        freq = self.hist.sum(axis=1) / self.hist.sum()
        fwavacc = (freq[freq > 0] * iu[freq > 0]).sum()
        return acc, acc_cls, iu, mean_iu, fwavacc

    def evaluate_front(self):
        iou = self.hist[1,1] / (self.hist[1].sum() + self.hist[:,1].sum() - self.hist[1, 1])
        dice = 2 * self.hist[1,1] / (self.hist[1].sum() + self.hist[:,1].sum())
        return iou, dice


def max_connected_domain(pred, threshold):
    pred[pred >= threshold] = 255
    pred[pred < threshold] = 0
    pred = pred.astype(np.uint8)

    #label_img, num = measure.label(img, neighbors=8,background=0,return_num = True)
    label_img = measure.label(pred, connectivity=2)
    max_label, max_area = 0, 0
    properties = measure.regionprops(label_img)
    for prop in properties:
        if prop.area > max_area:
            max_label = prop.label
            max_area = prop.area
    if max_label != 0:
        pred[label_img == max_label] = 1 
        pred[label_img != max_label] = 0
    return pred
    

def max_prob_domain(pred, threshold):
    orig_pred = copy.deepcopy(pred) 
    pred[pred >= threshold] = 255
    pred[pred < threshold] = 0
    pred = pred.astype(np.uint8)

    #label_img, num = measure.label(img, neighbors=8,background=0,return_num = True)
    label_img = measure.label(pred, connectivity=2)
    max_label, max_avg_prob = 0, 0
    properties = measure.regionprops(label_img)
    for prop in properties:
        coords = prop.coords
        sum_num = sum([orig_pred[i,j] for i, j in coords])
        avg_prob = sum_num / prop.area
        if avg_prob > max_avg_prob:
            max_label = prop.label
            max_avg_prob = avg_prob 
    if max_label != 0:
        pred[label_img == max_label] = 1 
        pred[label_img != max_label] = 0
    return pred


def main():
    args = parse_args() 
    mask_list = glob.glob(args.pred_path + '/*.jpg')
    iou_list, dice_list = [], [] 
    for pred_path in mask_list:
        name = os.path.basename(pred_path)
        name = name.split('.')[0] + '.tif'
        gt_path = os.path.join(args.gt_path, name)

        metrics = IOUMetric(args.num_classes, args.threshold)
        pred = cv2.imread(pred_path, 0)
        pred = np.asarray(pred)
        label = cv2.imread(gt_path, 0)
        label = np.asarray(label)

        if args.connected_domain:
            pred = max_connected_domain(pred, 125)
        else:
            pred[pred >= 125] = 255
            pred[pred < 125] = 0
            pred[pred==255] = 1
        metrics.add_batch(pred, label)
        iou, dice = metrics.evaluate_front()
        iou_list.append(iou)
        dice_list.append(dice)
    avg_iou, avg_dice = sum(iou_list) / len(iou_list), sum(dice_list) / len(dice_list)
    print('mean iou: {}, mean dice: {}'.format(avg_iou, avg_dice))
    print('Done.')


if __name__ == '__main__':
    main() 
