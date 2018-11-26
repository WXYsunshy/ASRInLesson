import os
import re
import python_speech_features
import scipy.io.wavfile as wav
import numpy as np
import csv
audio_path = 'E:/项目/ASRInLesson/same_segment_1'

mfcc_path= 'E:/项目/ASRInLesson/mfcc_16/'
if not os.path.exists(mfcc_path):
    os.makedirs(mfcc_path)
audio_list = os.listdir(audio_path)
audio_list.sort(key=lambda x:str(x[:-4]))

for i in audio_list:
    signal_name = os.path.join(audio_path, i)
    rate, data = wav.read(signal_name)
    try:
        mfcc = python_speech_features.mfcc(data,rate,numcep=16) #取倒谱系数13
        #delta1= python_speech_features.delta(mfcc,1)#一阶差分
        #delta2= python_speech_features.delta(mfcc,2)#二阶差分
        #mfcc_delta = np.hstack((mfcc,delta1,delta2))#拼接矩阵
    except:
        print(i)
    else:
        with open((mfcc_path + i).replace('wav', 'csv'), 'w',newline='') as fobj:
            writer = csv.writer(fobj)
            #writer.writerows(mfcc_delta)
            writer.writerows(mfcc)#取向量的2~16列