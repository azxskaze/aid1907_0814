import random1
scor=0
sum_value=0
for i in range(5):
    num01=random1.randint(1, 100)
    num02=random1.randint(1, 100)
    print(num01,'+',num02,'=:')
    sum_value=int(input('请输入答案：'))
    if sum_value == num02+num01:
        scor+=20
        print('答对了！')
    else:
        print('答错了！')
print('得分是：',scor)