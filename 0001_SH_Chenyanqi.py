# homework_0001
# 定义一个函数，获取一段字符串中紧跟在the name is 后，逗号前的人名
def getName(srcStr):
	index1 = srcStr.find('the name is')
	index2 = srcStr.find(',',index1)
	index1 += 12

	print srcStr[index1:index2]