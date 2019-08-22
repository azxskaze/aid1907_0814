def fun():
    while True:
        try:
            i=float(input('请输入成绩'))
            if 100>i>0:
                return i
            else:
                raise ValueError('7777777777')
        except ValueError as e:
            print(e)
    # '''接受所有异常'''
        except Exception:
            print('输入有误')

if __name__=='__main__':
    print(fun())


