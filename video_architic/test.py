from class_model.forward_gpu import *

classfic = Classification(4, './class_model/model_best.pth.tar')
classfic('/home/tiger/dataset/test_yz')