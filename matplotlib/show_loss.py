import os
import numpy as np
import matplotlib.pyplot as plt

# plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签 
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

f = open("/Users/bytedance/Documents/log/simple.log")
line = f.readline()
loss = []
count = 0
while line:
    if line != "\n":
        loss.append(float(line.split()[-1]))
    line = f.readline()

f.close()

x = np.arange(len(loss))

plt.plot(x[100::10], loss[100::10], color='red', label='loss')

plt.title(u'loss curve')
plt.xlabel(u'iter')
plt.ylabel(u'loss')

plt.legend()
plt.show()
