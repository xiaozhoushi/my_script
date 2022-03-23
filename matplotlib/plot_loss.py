import os
import pandas as pd
import math
import numpy as np
import matplotlib.pyplot as plt
import json


def plot_curve(x_vals, y_vals, x2_vals = None, y2_vals = None, title = None):
    #plt.rcParams["font.family"] = "Kaiti"
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    #plt.semilogy(x_vals, y_vals, 'r-', label = 'train loss')
    plt.plot(x_vals, y_vals, 'r-', label = 'train loss')
    if x2_vals and y2_vals:
        #plt.semilogy(x2_vals, y2_vals, 'c-', label = 'validation loss')
        plt.plot(x2_vals, y2_vals, 'c-', label = 'validation loss')
    plt.legend()
    if title:
        plt.title(title)
    plt.savefig('./' + title + '.png')

def smooth_loss(loss, weight = 0.2):
    last = loss[0]
    for i in range(len(loss)):
        loss[i] = last * weight + (1 - weight) * loss[i]
        last = loss[i]


def main():
    file_path = '/Users/bytedance/Documents/log/changweijingfenlei.txt'
    x_val, y_val, x2_val, y2_val = [], [], [], []
    
    # simple
    # with open(file_path, 'r') as f:
    #     lines = f.readlines()
    #     lenght = math.ceil(len(lines) / 760)
    #     for i in range(lenght):
    #         train_loss, val_loss = [], [] 
    #         for j in range(750):
    #             index = i * 760 + j
    #             if index >= len(lines):
    #                 break
    #             line = lines[index].strip()
    #             train_loss.append(float(line.split()[-1]))
    #         for j in range(10):
    #             index = i * 760 + 750 + j
    #             if index >= len(lines):
    #                 break
    #             line = lines[index].strip()
    #             val_loss.append(float(line.split()[-1]))
    #         if len(train_loss):
    #             x_val.append(i)
    #             y_val.append(sum(train_loss) / len(train_loss))
    #         if len(val_loss):
    #             x2_val.append(i)
    #             y2_val.append(sum(val_loss) / len(val_loss))
    #     smooth_loss(y_val)
    #     smooth_loss(y2_val)
    #     plot_curve(x_val, y_val, x2_val, y2_val, 'Cavity Positioning')

    # hard
    # df = pd.read_csv(file_path, skiprows = 0, usecols=['train_loss', 'eval_loss'])
    # lenght = df.shape[0]
    # for i in range(lenght):
    #     x_val.append(i)
    #     y_val.append(df.iat[i, 0])
    #     x2_val.append(i)
    #     y2_val.append(df.iat[i, 1])
    # smooth_loss(y_val)
    # smooth_loss(y2_val)
    # plot_curve(x_val, y_val, x2_val, y2_val, 'Cavity aware')

    # 回盲识别
    # with open(file_path, 'r') as js:
    #     lines = js.readlines()
    #     for i in range(len(lines)):
    #         data_dict = eval(lines[i])
    #         x_val.append(i)
    #         y_val.append(data_dict['train loss'])
    #         x2_val.append(i)
    #         y2_val.append(data_dict['val loss'])
    #     smooth_loss(y_val)
    #     smooth_loss(y2_val)
    #     plot_curve(x_val, y_val, x2_val, y2_val, 'lleocecal valve recognition')
            
    # 粘膜覆盖度
    # df = pd.read_csv(file_path, skiprows = 0, usecols=['train_loss', 'eval_loss'])
    # lenght = df.shape[0]
    # for i in range(lenght):
    #     x_val.append(i)
    #     y_val.append(df.iat[i, 0])
    #     x2_val.append(i)
    #     y2_val.append(df.iat[i, 1])
    # smooth_loss(y_val)
    # smooth_loss(y2_val)
    # plot_curve(x_val, y_val, x2_val, y2_val, 'Mucociliary coverage')

    # 清洁度
    # df = pd.read_csv(file_path, skiprows = 0, usecols=['train_loss', 'eval_loss'])
    # lenght = df.shape[0]
    # for i in range(lenght):
    #     x_val.append(i)
    #     y_val.append(df.iat[i, 0])
    #     x2_val.append(i)
    #     y2_val.append(df.iat[i, 1])
    # smooth_loss(y_val)
    # smooth_loss(y2_val)
    # plot_curve(x_val, y_val, x2_val, y2_val, 'Cleanliness evaluation')

    # poly class
    # with open(file_path, 'r') as f:
    #     lines = f.readlines()
    #     epoch = 0
    #     for line in lines:
    #         if 'Training' in line and 'loss' in line:
    #             epoch += 1
    #             loss = float(line.split()[-4])
    #             x_val.append(epoch)
    #             y_val.append(loss)
    #         if 'Validation' in line and 'loss' in line:
    #             loss = float(line.split()[-4])
    #             x2_val.append(epoch)
    #             y2_val.append(loss)
    #     smooth_loss(y_val)
    #     smooth_loss(y2_val)
    #     plot_curve(x_val, y_val, x2_val, y2_val, 'Polyp Classfication')


    # poly detection 
    # with open(file_path, 'r') as f:
    #     lines = f.readlines()
    #     epoch = 0
    #     for line in lines:
    #         if 'Training' in line and 'loss' in line:
    #             epoch += 1
    #             loss = float(line.split()[-11])
    #             x_val.append(epoch)
    #             y_val.append(loss)
    #         #if 'Validation' in line and 'sen@0.5' in line:
    #         #    loss = float(line.split()[-2])
    #         #    x2_val.append(epoch)
    #         #    y2_val.append(loss)
    #     smooth_loss(y_val)
    #     #smooth_loss(y2_val)
    #     #plot_curve(x_val, y_val, x2_val, y2_val, 'Polyp Detection')
    #     plot_curve(x_val, y_val, title = 'Polyp Detection')


    # 肠胃镜分类  
    with open(file_path, 'r') as f:
        lines = f.readlines()
        epoch = 0
        for line in lines:
            if 'train loss' in line:
                epoch += 1
                loss = float(line.split()[-1])
                x_val.append(epoch)
                y_val.append(loss)
        smooth_loss(y_val)
        plot_curve(x_val, y_val, title = 'Gastrointestinal Classification')


if __name__ == '__main__':
    main()
