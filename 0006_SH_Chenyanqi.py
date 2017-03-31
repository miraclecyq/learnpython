# -*- coding:utf-8 -*-
# 第六次编程作业

# phone文件夹在同一个目录下作为包调用
from phone.apple import askPrice as iphone6
from phone.apple import askPrice as iphone7
from phone.samsung import askPrice as note7
from phone.samsung.s.galaxy_s7 import askPrice as s7

iphone6()
iphone7()
note7()
s7()
# phone文件夹在不同目录下作为包调用
# import sys
# sys.path.append('//Users//cyq//study//pythonwork//phone//')
# print sys.path
# import apple.iphone6 as iphone6
# import apple.iphone7 as iphone7
# import samsung.note.galaxy_note7 as note7
# import samsung.s.galaxy_s7 as s7
#
# iphone6.askPrice()
# iphone7.askPrice()
# note7.askPrice()
# s7.askPrice()