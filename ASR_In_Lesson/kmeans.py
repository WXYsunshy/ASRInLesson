import os
from sklearn.cluster import KMeans
from sklearn.externals import joblib
from sklearn.preprocessing import Imputer
from sklearn import cluster
import numpy as np
import pandas as pd
from itertools import islice
#for line in islice(f0, 1, None):  
#    data=pd.read_csv(f0,usecols=[1])
#显示所有列
pd.set_option('display.max_columns', None)
#显示所有行
pd.set_option('display.max_rows', None)
CS_path='E:/项目/ASRInLesson/CS_mfcc/'
csv_path='E:/项目/ASRInLesson/mfcc_16/'
csv_list=os.listdir(csv_path)
#print(csv_list.shape)
T='E:/项目/ASRInLesson/CS_mfcc/CS_T.csv'
f0 = open(T)
data=pd.read_csv(f0,header=0,usecols=[1])
ID=[]
for obj in csv_list:
    ID.append(obj)
print(len(ID))
#print (data)
data=np.array(data)
print(data.shape)
#data = Imputer(strategy='median').fit_transform(data)
#np.set_printoptions(threshold='nan')
#print (data)

# 聚类为2类
estimator=KMeans(n_clusters=2)
# fit_predict表示拟合+预测，也可以分开写
res=estimator.fit_predict(data)
# 预测类别标签结果
lable_pred=estimator.labels_
lable=[]
lable=lable_pred
lable=lable.reshape(-1,1)
print(lable.shape)
#print(type(lable))
# 各个类别的聚类中心值
centroids=estimator.cluster_centers_
# 聚类中心均值向量的总和
inertia=estimator.inertia_
 
print (lable_pred)
print (centroids)
print (inertia)

test=pd.DataFrame(index=ID,data=lable)
#test=pd.DataFrame({'ID':ID,'CS':data,'lable':lable})
#print(test.type)'ID':csv_list,
test.to_csv(CS_path+'predict_CS_T.csv',float_format='%.8f',encoding='gbk')
#predict = np.hstack((csv_list,data,lable))