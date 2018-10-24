import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import csv
i=14 #i表示对比特征第几列
filename_T1='E:/项目/ASRInLesson/mfcc_2_16/audio1_TS.csv'
with open(filename_T1) as f: #打开文件文件并将内容储存在reader中
    csv_data=csv.reader(f) #读取并将内容储存在reader中
    list_str = [row[i] for row in csv_data]   #读取每列的数据
    list_float = list(map(lambda x:float(x), list_str)) #将list中的字符转为数字
    #print(list_float)
    T1,=plt.plot(list_float,color = 'blue',linewidth=2,linestyle='-')
    
filename_T2='E:/项目/ASRInLesson/mfcc_2_16/audio41_T.csv'
with open(filename_T2) as f: #打开文件文件并将内容储存在reader中
    csv_data=csv.reader(f) #读取并将内容储存在reader中
    list_str = [row[i] for row in csv_data]   #读取每列的数据
    list_float = list(map(lambda x:float(x), list_str)) #将list中的字符转为数字
    #print(list_float)
    T2,=plt.plot(list_float,color = 'red',linewidth=2, linestyle='-')

filename_S1='E:/项目/ASRInLesson/mfcc_2_16/audio46_S.csv'
with open(filename_S1) as f: #打开文件文件并将内容储存在reader中
    csv_data=csv.reader(f) #读取并将内容储存在reader中
    list_str = [row[i] for row in csv_data]   #读取每列的数据
    list_float = list(map(lambda x:float(x), list_str)) #将list中的字符转为数字
    #print(list_float)
    S1,=plt.plot(list_float,color = 'green',linewidth=2, linestyle=':')  
filename_S2='E:/项目/ASRInLesson/mfcc_2_16/audio47_S.csv'
with open(filename_S2) as f: #打开文件文件并将内容储存在reader中
    csv_data=csv.reader(f) #读取并将内容储存在reader中
    list_str = [row[i] for row in csv_data]   #读取每列的数据
    list_float = list(map(lambda x:float(x), list_str)) #将list中的字符转为数字
    #print(list_float)
    S2,=plt.plot(list_float,color = 'black',linewidth=2, linestyle=':')
plt.xlabel('time')
plt.ylabel('value')
plt.title(i)
plt.legend([T1,T2,S1,S2],["T_1","T_2","S_1","S_2"] ,loc=1)
plt.show()
