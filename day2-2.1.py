# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 10:44:10 2020

@author: AE401
"""

import random
n = random.randint(1,20)
v=0
while True:
    b = input("請輸入數字")
    b = int(b)
    v=v+1                                       
    if b>20 or b<0:
        print('錯誤')
    else:
        if b > n:
            print('小一點')
        elif b < n:
            print('大一點')
        else:
            print('bingo')
            break
    if v>4:
        print('超過次數')
        break