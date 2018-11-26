#rom sklearn.metrics.pairwise import cosine_similarity
from scipy.spatial import distance
#from sklearn import preprocessing
import numpy as np
import pandas as pd
import csv
import os
import re

#显示所有列
#pd.set_option('display.max_columns', None)
#显示所有行
pd.set_option('display.max_rows', None)
T='E:/项目/ASRInLesson/mfcc_16/016_T.csv'
f0 = open(T)
cos1=pd.read_csv(f0,header=None)
cos1=np.array(cos1)
cos1=cos1.reshape(-1)[:1300]
CS_path='E:/项目/ASRInLesson/CS_mfcc/'
if not os.path.exists(CS_path):
    os.makedirs(CS_path)
csv_path='E:/项目/ASRInLesson/mfcc_16/'
csv_list=os.listdir(csv_path)
#csv_list.sort(key=lambda x:str(x[:-4]))#按照大小排序
#匹配关键字
key = '.*_.*' #匹配所有师生的特征
#key = '.*_T.*' #匹配所有老师的特征
#key = '.*_S.*' #匹配所有学生的特征
objective_list = []
for obj in csv_list:
    if re.match(key, obj):
        objective_list.append(obj)
print(len(objective_list))
#print(csv_list)
list = []
for f in objective_list:
    print(f)
    if f[-4:]=='.csv':
        f1 = open(csv_path + f)
        cos2 = pd.read_csv(f1,header=None)
        cos2=np.array(cos2)
        cos2=cos2.reshape(-1)[:1300]
        cs=1 - distance.cosine(cos1,cos2)
        #cs=cosine_similarity(cos1,cos2)
        print(cs)
        #print(type(cs[1]))
        list.append(cs)
        #print(list[0])
        #print(type(list))
print(len(objective_list))
#print(list)
test=pd.DataFrame(index=objective_list,data=list)
#print(test.type)
test.to_csv(CS_path+'CS_T.csv',float_format='%.8f',encoding='gbk')

