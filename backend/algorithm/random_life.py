#-*- coding : utf-8 -*-
# coding: utf-8

import sys
import os

if len (sys.argv) < 2:
    print("Usage: python random_life.py <excelfile>")
    sys.exit(1)

excel_file = sys.argv[1]
file_name, ext = os.path.splitext(excel_file)
# 生成随机整数，范围在1~70
import random
print(random.randint(1,70),end='')
