# -*- coding: utf-8 -*-
"""
Created on Sat Sep 09 09:57:15 2017

@author: zchenack
"""

import os
import numpy as np
import pandas as pd
from pyecharts import Line

def Getfile(dirName):
    '''
    获取文件夹数据
    '''
    files = os.listdir(dirName)
    return files

def ReName(path,files):
    '''
    文件重命名
    '''
    for f in files:
        os.rename(dirName+f,dirName+f[9:])

def PlotLine(line,datx,daty,Marker):
    '''
    绘制线型图像
    '''
    #line = Line(Title)
    line.add(Marker,datx,daty, mark_point=["average","max"])
    #return line
    #line.show_config()
    #line.render()

def CalIncRate(NewFiles):
    '''
    计算每日增长基金占比
    '''
    dayInc = []
    dayIncVal = []
    mk = 0
    for f in NewFiles:
        mk += 1
        print mk
        data = pd.read_html(dirName+f)
        Inc = data[0][5][1:]
        IncVal = map(float,data[0][4][1:])
        dayIncVal.append(sum(IncVal))
        cnt = 0
        for rate in Inc:
            if float(rate) > 0:
                cnt += 1
        dayInc.append(cnt/float(len(Inc)))
    return dayInc,dayIncVal,np.cumsum(dayIncVal)

def CalIncNum(NewFiles):
    '''
    计算每日总基金增长点
    '''
    dayIncNum = []
    return dayIncNum

dirName = u'./股票型基金/'

NewFiles = Getfile(dirName)
dayInc,dayIncVal,dayIncCum = CalIncRate(NewFiles)

line = Line("每日增长基金占比","3月-8月")
PlotLine(line,range(len(dayInc)),dayInc,"比例")
line.show_config()
line.render('h1.html')

line = Line("每日基金增长总量","3月-8月")
PlotLine(line,range(len(dayInc)),dayIncVal,"增长量")
line.show_config()
line.render('h2.html')

line = Line("基金累计增长总量","3月-8月")
PlotLine(line,range(len(dayInc)),list(dayIncCum),"增长累积量")
line.show_config()
line.render('h3.html')