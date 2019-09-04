'''空洞文件'''
f = open('2.txt','w')
f.write('a')
f.seek(1024*1024*10+1)
f.write('b')
f.close()