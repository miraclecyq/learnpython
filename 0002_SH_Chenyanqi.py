# -*- coding:utf-8 -*-
# 第二次编程作业
# 提示用户输入如下格式内容Jack Green, 21 ; Mike Mos, 9;后,分行打印学生信息,要求,姓名左对齐宽度20,年龄右对齐,宽度2,不足补零
stu_info = raw_input('please enter students\' name and age :').split(';')
for one in stu_info:
    if one == '' or one.count(',') != 1:
        break
    one = one.split(',')
    one[0] = one[0].strip()
    one[1] = one[1].strip()
    print '%-20s: %02d' % (one[0], int(one[1]))


