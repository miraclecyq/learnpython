# -*- coding:utf-8 -*-
# 第三次编程作业
# 将传入列表中数字从小到大排列在新列表中
print "ok"
def bubble(alist):
    newList=[]
    for i in range(len(alist)):
        listMin=min(alist)
        newList.append(listMin)
        alist.remove(listMin)
    return newList