# encoding=utf8
def getDict(filepath, a, b):
    with open(filepath) as file:
        file.readline()  #读取第一行后,指针指到第二行开头
        content = file.readlines()
        dict = {}
        for one in content:
            key, value = one.split(';')[a], one.split(';')[b].replace('\r\n','')
            if key in dict:
                dict[key].append(value)
            else:
                dict[key] = [value]
        return dict

course = getDict('0008/course.txt', 0, 1)
teacher = getDict('0008/teacher.txt', 0, 4)
teacher_course = getDict('0008/teacher_course.txt', 0, 1)

for t_id, c_ids in teacher_course.items():
    print teacher[t_id][0], ':'
    for c_id in c_ids:
        print course[c_id][0]
    print '\n'