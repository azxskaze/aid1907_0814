dict01={
    '北京':{'美食':['烤鸭','豆汁','卤煮','炸酱面'],
           '景区':['故宫','天安门','天坛']},

    '四川': {
            '美食': [ '火锅', '串串', '毛血旺'],
            '景区': ['峨眉山', '九寨沟', '春熙路']}
}
for city in dict01:
    for food in dict01[city]:
        if food=='美食':
            for menu in dict01[city][food]:
                print(city,menu)
