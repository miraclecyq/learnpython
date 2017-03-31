# -*- coding:utf-8 -*-
# 第五次编程作业
# 整理学生签到表

def putInfoToDict(fileName):

    checkinDict = {}

    with open(fileName) as f:
        checkinlist = f.read()
        percheckin = checkinlist.splitlines()

    for one in percheckin:
        #将每行签到信息中的checkintime,lessonid,userid提取出来
        one = one.replace('(','').replace('),','').replace("'",'').replace(');','')
        info = one.split(',')
        checkintime = info[0].strip()
        lessonid    = info[1].strip()
        userid      = info[2].strip()

        #将签到信息填入checkinDict
        if userid not in checkinDict:
            checkinDict[userid] = [{'lessonid':lessonid,'checkintime':checkintime}]
        else:
            checkinDict[userid].append({'lessonid':lessonid,'checkintime':checkintime})
    return checkinDict
#     import pprint
#     pprint.pprint(checkinDict)
# putInfoToDict('0005_1.txt')





