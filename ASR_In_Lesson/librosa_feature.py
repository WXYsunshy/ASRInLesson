import librosa
import librosa.display
import matplotlib.pyplot as plt
audio = 'E:/项目/ASRInLesson/same_segment/audio1_TS.wav'
y, sr = librosa.load(audio,sr=None)
mfccs = librosa.feature.mfcc(y=y, sr=sr,n_mfcc=13)
print(mfccs)
print(mfccs.shape)

