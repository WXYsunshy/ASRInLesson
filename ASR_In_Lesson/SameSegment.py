from pydub import AudioSegment
import os, re
import wave
# 循环目录下所有文件
audio_path='E:/项目/ASRInLesson/TimeSegment'
output_path='E:/项目/ASRInLesson/same_segment_1'
if not os.path.exists(output_path):
    os.makedirs(output_path)
audio_list = os.listdir(audio_path)
audio_list=os.listdir(audio_path)
audio_list.sort(key=lambda x:str(x[:-4]))
print(audio_list)
for audio in audio_list:
    if audio[-4:]=='.wav':
        this_path_input=os.path.join(audio_path,audio)
        this_path_output=os.path.join(output_path,audio[:-4]+'.wav')
        wav = AudioSegment.from_wav(this_path_input) # 打开wav文件
        wav[:1*1000].export(this_path_output, format="wav") # 切割前1秒并覆盖保存
print(len(audio_list))