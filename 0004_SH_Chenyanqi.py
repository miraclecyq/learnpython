# -*- coding:utf-8 -*-
# 第四次编程作业
# 计算所有员工税后工资和扣税明细保存到新文件2

with open('file1.txt') as f: #打开file1.txt
    f1 = f.read().split('\r\n')
with open('file2.txt','w') as f2: #打开新文件file2.txt
    index=0
    while index < len(f1):
        per = f1[index].split(';') #以分号将每个人的姓名和薪资分隔
        perList = per[0].split(':')+per[1].split(':') #将per中的姓名和薪资再以冒号分隔重组传给变量perList
        # 获得每个人的姓名,薪资,实际收入,扣税金额
        name = perList[1].strip()
        salary = int(perList[3].strip())
        income = int(salary*0.9)
        tax = int(salary - income)
        f2.write('name:%5s; salary:%6d; tax:%5d; income:%6d\r\n'%(name,salary,tax,income))
        f2.flush()
        index += 1