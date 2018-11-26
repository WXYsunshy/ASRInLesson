import pandas as pd
import numpy as np
import csv
import os
import re
#目标样本文件T
#T1='E:/项目/ASRInLesson/mfcc_feature_delta1_delta2/016_T.csv'
T1='E:/项目/ASRInLesson/mfcc_feature_delta1_delta2/016_T.csv'
#待匹配文件路径
T2='E:/项目/ASRInLesson/mfcc_feature_delta1_delta2/'
#保存路径
ED_path='E:/项目/ASRInLesson/ED_mfcc/'
#打开样本文件
f0 = open(T1)
list_float1=pd.read_csv(f0,header=None)
v1 = list_float1
#print(list_float1.shape)
csv_path='E:/项目/ASRInLesson/mfcc_feature_delta1_delta2'
csv_list=os.listdir(csv_path)
#csv_list.sort(key=lambda x:str(x[:-4]))#按照大小排序
#匹配关键字
key = '.*_.*' #匹配所有老师的特征
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
        f1 = open(T2 + f)
        v2 = pd.read_csv(f1,header=None)
        dist = np.linalg.norm(v1 - v2)
        print(dist)
        #print(type(dist))
        list.append(dist)
        #print(list)
        #with open(ED_path+'ED.csv','w',newline='') as csvfile:
        #with open((ED_path + i ).replace('csv', 'csv'), 'w',newline='') as csvfile:
            #print(type(csvfile))
            #writer = csv.writer(csvfile)
            #writer.writerow(["identity", "ED"])
            #writer.writerows([[f, dist]])
            #for row in list:
                #writer.writerow(row)
           # for i in range(len(csv_list)):
               # writer.writerows([[f, dist]])
print(len(objective_list))
#print(list)
test=pd.DataFrame(index=objective_list,data=list)
#print(test)
test.to_csv(ED_path+'ED_T.csv',encoding='gbk')
