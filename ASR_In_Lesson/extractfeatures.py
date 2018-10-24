import os
from python_speech_features import mfcc
from python_speech_features import logfbank
import scipy.io.wavfile as wav
import numpy as np

audio_path = 'E:/项目/ASRInLesson/ASR_In_Lesson/ASR_In_Lesson/segment'
n=0
save_path = 'E:/项目/ASRInLesson/ASR_In_Lesson/ASR_In_Lesson/feature'
if not os.path.exists(save_path):
    os.makedirs(save_path)
for audio in audio_path:
    if audio[-4:]=='.wav':
        file_feature = open(save_path+audio[:-4]+'.txt','a+')
        (rate,sig) = wav.read(audio_path)
        try:
            mfcc_feat = mfcc(sig,rate)
            file_feature.write(str(mfcc_feat)+'\n')
        except:
            print(audio_path)
            continue
            file_feature.close()