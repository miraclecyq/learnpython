# encoding=utf8
filename=raw_input('请输入新文件的名称:')
f1=open('cfiles/gbk编码.txt')
f1gbk=f1.read().decode('gbk')
f1.close()
f2=open('cfiles/utf8编码.txt')
f2utf8=f2.read().decode('utf8')
f2.close()
fall=f1gbk+'\n'+f2utf8
print fall
fnew=open(filename,'w')
fnew.write(fall.encode('utf8'))
fnew.flush()
fnew.close()
