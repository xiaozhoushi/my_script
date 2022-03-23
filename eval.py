import csv
import os
from sklearn.metrics import roc_curve, auc, accuracy_score, precision_score, f1_score, recall_score, confusion_matrix


def is_image_file(filename):
    return any(filename.endswith(extension) for extension in ['.png', '.jpg', '.jpeg', '.PNG', '.JPG', '.JPEG'])


def evaluation(pred, label):
    acc = accuracy_score(label, pred)
    precision = precision_score(label, pred, zero_division = 1)
    f1 = f1_score(label, pred, zero_division = 1)
    recall = recall_score(label, pred)
    matrix = confusion_matrix(label, pred)
    return acc, precision, f1, recall, matrix

def main():
    img_path = '/Users/bytedance/Documents/Documents/data/images/classfication/test'
    csv_path = '/Users/bytedance/Documents/Documents/data/images/classfication/biankuang_blur_black_bgr.csv'
    dataset = []
    for img_root, _, img_names in os.walk(img_path):
        tmp = img_root.split('/')
        label = None
        for item in tmp[::-1]:
            if item == '0' or item == '1' or item == '2':
                label = item
        if label is None:
            continue
        label = int(label)
        data_tmp = [[name, label] for name in img_names if is_image_file(name)]
        dataset += data_tmp

    n_total = len(dataset)
    print('data set lenght:', n_total)

    pred_dic = {}
    with open(csv_path, 'r') as f:
        csv_data = csv.reader(f)
        for i, item in enumerate(csv_data):
            if i == 0:
                continue
            label = 0
            if float(item[3]) < 0.5 and float(item[2]) < 0.5:
                label = 1
            pred_dic[item[0]] = label
    
    labels = []
    predict = []
    num = 0
    for item in dataset:
        if item[0] in pred_dic.keys():
            if item[1] == 2:
                item[1] = 0
                if pred_dic[item[0]] == 1:
                    num += 1
            labels.append(item[1])
            predict.append(pred_dic[item[0]])
    acc, precision, f1, recall, matrix = evaluation(predict, labels)
    print('number:', num)
    print('evaluation: acc: {}, precision: {}, f1: {}, recall: {}, matrix: {}.'.format(acc, precision, f1, recall, matrix))

if __name__ == '__main__':
    main()
        
