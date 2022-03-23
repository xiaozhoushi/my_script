### 根据md5值去重
import os,sys
import hashlib

import numpy as np
from multiprocessing import Pool

def get_md5(file_name):
    with open(file_name, 'rb') as fp:
        data = fp.read()
    return [file_name, hashlib.md5(data).hexdigest()]

def deduplication(file_names):
	pool = Pool(processes=4)

	rslt = pool.map(get_md5, file_names)

	pool.close()
	pool.join()


	files_dup = []
	md5_dup = []
	for i, (file_name, md5) in enumerate(rslt):
	    if md5 not in md5_dup:
	        md5_dup.append(md5)
	        files_dup.append(file_name)
	
	return files_dup
