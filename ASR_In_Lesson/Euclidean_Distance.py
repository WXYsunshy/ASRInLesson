import pandas as pd
import numpy 
import csv
#计算欧氏距离公式
def EuclideanDistance(vec1,vec2):
    dist = numpy.sqrt(numpy.sum(numpy.square(vec1 - vec2)))
    return dist
T1='E:/项目/ASRInLesson/mfcc_feature/audio6_T.csv'
f0=open(T1)
list_float1=pd.read_csv(f0,header=None)
#print(list_float1.shape)
T2='E:/项目/ASRInLesson/mfcc_feature/audio73_T.csv'
f1=open(T2)
list_float2=pd.read_csv(f1,header=None)
#with open(T2) as f: #打开文件文件并将内容储存在reader中
    #csv_data=csv.reader(f) #读取并将内容储存在reader中
    #list_str = [row for row in csv_data]   #读取每列的数据
    #list_float2 = list(map(lambda x:float(x), list_str)) #将list中的字符转为数字
    #list_float2 = list(csv_data)
    #list_float2=pd.read_csv(f)
v1 = list_float1
v2 = list_float2
#v1 = numpy.array(v1)
#v2 = numpy.array(v2)
dist = numpy.linalg.norm(v1 - v2)
#print (EuclideanDistance(v1,v2))
print(dist)