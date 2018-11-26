#!/usr/bin/env python
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from itertools import product
from librosa import load
from pyvad import vad, trim
import numpy as np
fs_vads = (8000, 16000, 32000, 48000)
hops = (10, 20, 30)
vad_modes = (0, 1, 2, 3)

#name ='E:/项目/ASRInLesson/lessons/test05mi.wav'
name='E:/项目/ASRInLesson/same_segment/audio77_T.wav'
data, fs = load(name, sr=None)
time = np.linspace(0, len(data)/fs, len(data)) # time axis
fig, ax0 = plt.subplots()
plt.plot(time, data)

#plt.show()

for fs_vad, hop, vad_mode in product(fs_vads, hops, vad_modes):
    vact = vad(data, fs, fs_vad=16000, hoplength=30, vad_mode=0)
 
fig, ax1 = plt.subplots()
ax1.plot(time, data, color = 'b', label='speech waveform')
ax1.set_xlabel("TIME [s]")

ax2=ax1.twinx()
ax2.plot(time, vact, color="r", label = 'vad')
plt.yticks([0, 1] ,('unvoice', 'voice'))
ax2.set_ylim([-0.01, 1.01])

plt.legend()

#plt.show()

#输出剪切之后的音频
trimed = trim(data, fs, fs_vad = 16000, hoplength = 30, vad_mode=3)
time = np.linspace(0, len(trimed)/fs, len(trimed)) # time axis
fig, ax1 = plt.subplots()

ax1.plot(time, trimed, color = 'b', label='speech waveform')
ax1.set_xlabel("TIME [s]")

plt.show()

plt.plot(trimed)
plt.show()
