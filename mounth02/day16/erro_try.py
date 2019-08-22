'''input会出现这些错误：
进行计算时，不能用0做被除数
int（）不能转换带小数点的数字字符串和非数字字符串
用户不输入会导致后面变量没有绑定对象
'''
#分苹果
def civ_apple(app_count):
    person_count=int(input('请输入人数'))
    res = app_count/person_count
    print(res)
if __name__=='__main__':
    try:
        civ_apple(10)
        '''可能出现异常的语句'''
    except ValueError:
        print('int')
    except ZeroDivisionError:
        print('0')
    except KeyboardInterrupt:
        print('用户中断输入')
    except Exception:
        '''将不知道的错误类型写到Exception里面'''
        print('未知错误')
    else:
        '''没有发生异常执行的语句'''
        print('nice')
    finally:
        '''不论有没有发生异常都会执行的语句'''
        print('over')
