import os
import re
import python_speech_features
import scipy.io.wavfile as wav
import numpy as np
import csv
audio_path = 'E:/项目/ASRInLesson/same_segment'
#目标关键字
key = '^audio.*'
#保存特征路径
mfcc_path= 'E:/项目/ASRInLesson/mfcc_delta_feature/'
if not os.path.exists(mfcc_path):
    os.makedirs(mfcc_path)
audio_list = os.listdir(audio_path)
objective_list = []
#寻找匹配关键字的音频
for obj in audio_list:
    if re.match(key, obj):
        objective_list.append(obj)
print(len(objective_list))
#提取特征
for i in objective_list:
    signal_name = os.path.join(audio_path, i)
    rate, data = wav.read(signal_name)
    try:
        mfcc = python_speech_features.mfcc(data, rate)
        delta= python_speech_features.delta(mfcc,1)
        mfcc_delta = np.hstack((mfcc,delta))
    except:
        print(i)
    else:
        with open((mfcc_path + i).replace('wav', 'csv'), 'w',newline='') as fobj:
            writer = csv.writer(fobj)
            writer.writerows(mfcc_delta)
