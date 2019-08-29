f = open('/home/tarena/PycharmProjects/aid1907/stage2/day04/1_tcp数据包.png','rb')
f2 = open('/home/tarena/PycharmProjects/aid1907/stage2/day04/包.png','wb')
for line in f:
    f2.write(line)
f.close()
f2.close()
