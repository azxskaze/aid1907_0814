print(eval('1*2*3+5+9'))
'''
eval将字符串
当做一句代码去执行，
限制：只能执行一行表达式
'''
# eval('del a01')
#-->error
'''
不能识别语句，
只能执行表达式
'''
'''
exec()将字符串当成一段代码去运行
写在每个语句之间用;或者 \n 来分隔
'''
exec('a=11;b=20;print(a+b)')
str02='''
a=56
b=85

print(a+b)

'''
exec(str02)