import numpy
import scipy.io.wavfile
from matplotlib import pyplot as plt
from scipy.fftpack import dct
audio='E:/项目/ASRInLesson/same_segment/audio77_T.wav'
sample_rate,signal=scipy.io.wavfile.read(audio)
print(sample_rate,len(signal))
#读取前1s 的数据
signal=signal[0:int(1*sample_rate)]

plt.plot(signal)
plt.show()