#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
f = open(r'E:\项目\ASRInLesson\mfcc_feature\audio1_TS.csv')
data=pd.read_csv(f)
print(data)
mydis_ed=[]
for i in range(0,13):
    dis_ed = []
    for j in range(0,13):
        ed = np.sqrt(np.sum((data.ix[:,i] - data.ix[:,j]) ** 2))
        dis_ed.append(ed)
    mydis_ed.append(dis_ed)
print(mydis_ed)
mydis_ed = pd.DataFrame(mydis_ed)
mydis_ed.to_csv(r'E:\项目\ASRInLesson\Eudis\audio1_TS_dis.csv', encoding='utf-8', index=False)

