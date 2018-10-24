import json
from scipy.io import wavfile

json_filepath ='E:/项目/ASRInLesson/lessons/underground_forest.json'   # json文件路径
wav_filepath='E:/项目/ASRInLesson/lessons/地下森林断想.wav'   # wav文件路径
savepath ='E:/项目/ASRInLesson/time_segment/'    # 分割后保存文件路径


def get_segpoint(filepath):
	# 从json文件中读取分割的时间点
	file = open(filepath, 'rb')
	json_file = json.load(file)
	begin, end, identity = [], [], []
	for dict_info in json_file:
		begin.append(int(dict_info['bg']))
		end.append(int(dict_info['ed']))
		identity.append(dict_info['speaker'])
	return begin, end, identity


sr, y = wavfile.read(wav_filepath)   # 加载音频文件，sr为采样率，y是数据

bp, ep, identity = get_segpoint(json_filepath)   # 将从json中读取的分割点保存到两个列表
list=len(bp)
for i in range(list):
	temp_audio = y[int(bp[i]/1000*sr):int(ep[i]/1000*sr)]   # 按列表中的分割点先分割音频数据y
	wavfile.write(savepath+'audio%s_%s.wav' % (i, identity[i]), sr, temp_audio)   # 将音频数据转成音频文件
print(list)

