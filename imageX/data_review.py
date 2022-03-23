# coding=utf-8
import requests
import json
import hashlib
import uuid
from time import time, sleep
from multiprocessing import Pool


def get_headers():
    access_key = '' # 分配的access_key
    access_secret = '' # 分配的access_secret

    timestamp = str(int(time()))

    nonce = uuid.uuid1().hex
    _list = [access_secret, timestamp, nonce]
    _list.sort()
    signature = hashlib.sha1(''.join(_list).encode('utf-8')).hexdigest()
    headers = {
        'X-AccessKey': access_key,
        'X-Signature': signature,
        'X-Timestamp': timestamp,
        'X-Nonce': nonce
    }
    return headers


# def create_task():
#     files = ['/Users/bytedance/Documents/Documents/data/images/image_url.txt']
#     date = []
#     for file in files:
#         with open(file, 'r') as fin:
#             for line in fin:
#                 date.append(line.strip('\n'))
#             urls_str = ''
#             for i, datum in enumerate(date):
#                 #print('datum = {}'.format(datum))
#                 object_id, _, image_url = str(datum).split(',')
#                 urls_str += json.dumps(dict(url=image_url))
#                 if (i+1) % 8 == 0 and i != 0:
#                     r = requests.post('', data=dict(project_id='', \
#                     object_id=object_id, object_data=json.dumps(urls_str)),headers=get_headers(), verify=False)
#                     urls_str = ''
#             if len(urls_str):
#                 r = requests.post('', data=dict(project_id='', \
#                 object_id=object_id,object_data=json.dumps(urls_str)),headers=get_headers(), verify=False)
#             ret = r.text
#             print('ret', ret)
#             print(requests)
def review(i, datum):
    print('id = {}, datum = {}'.format(i, datum))
    object_name, image_url, _ = str(datum).split()
    _ = requests.post('/create_task/', data=dict(project_id='', \
    object_id=object_name, object_data=json.dumps(dict(url=image_url))),headers=get_headers(), verify=False)  ###############队列id



def create_task():
    files = ['imageX_30000.txt']
    data = []
    pool = Pool(processes=6)
    for file in files:
        with open(file, 'r') as fin:
            for line in fin:
                data.append(line.strip('\n'))
            #data = data[2830:]  ########中断后选择其实id
            for i, datum in enumerate(data):
                pool.apply_async(review, [i, datum])
    pool.close()
    pool.join()

if __name__ == '__main__':
    create_task()
