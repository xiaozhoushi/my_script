import pandas as pd
import os
import wget
import shutil

CSV_FILE = "/Users/Documents/data/label/5093248089816148491.csv"
df = pd.read_csv(CSV_FILE, skiprows=0, usecols=['对象id', '1_time'])
rows = df.shape[0]
cols = df.shape[1]
count = 0
print(df.head(5))
print("rows : ", rows, ", cols : ", cols)

if not os.path.exists('frames'):
    os.mkdir('frames')

for i in range(rows):
    obj_id = df.iat[i, 0]
    ori_time = df.iat[i, 1]
    if (ori_time.strip() == '' or ori_time is None):
        continue
    if (ori_time.count('{') == 2):
        continue

    start = ori_time.index('endtime')
    time = float(ori_time[ori_time.index(':', start) + 2 : ori_time.index(',', start)])
    index = int(time * 25)
    vid = obj_id.split('_')[0]
    print('\n', i, vid, time, index)

    filename = os.path.join('/Users/Documents/data/imageX_url/data 2', vid + '.txt')

    if os.path.exists(filename):
        img_ori = open(filename, 'r').read().splitlines()
        record = 0
        for img in img_ori:
            framepath = os.path.join('frames', vid + '_' + record)
            if not os.path.exists(framepath):
                os.mkdir(framepath)
            ind, url = img.split(' ')
            ind = int(ind)
            if ind <= index:
                break
            
            wget.download(url, out=os.path.join(framepath, vid + '_{}.jpeg'.format(ind)))
            index_num += 1
            if index_num == 100:
                record += 1
                index_num = 0
    else:
        print(filename, "文件不存在")
