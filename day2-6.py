# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 15:11:34 2020

@author: AE401
"""

names=list()
scores=list()
p=int(input('請輸入人數'))
for i in range(p):
    name=input('請輸入名子')
    names.append(name)
    a=input('成績')
    scores.append(a)

total=0
for i in scores:
    total=total+i
print("平均:",(total/p))


    