dict01={
    '北京：':[{'美食：':['烤鸭','豆汁','卤煮','炸酱面']},
           {'景区：':['故宫','天安门','天坛']}],
    '成都：': [{'美食：': [ '火锅', '串串', '毛血旺']},
            {'景区：': ['峨眉山', '九寨沟', '春熙路']}]
}


dict02={}
str01='this is a tese string'
for i in str01:
    if i not in dict02:
        dict02[i]=1
    else:
        dict02[i]+=1
print(dict02)


