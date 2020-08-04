# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 09:06:34 2020

@author: AE401
"""

import random
n = random.randint(1,10)
b = input('請輸入數字')
if b == n:
    print('bingo')
else:
    print('猜錯了')
