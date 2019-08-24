#
# def fun1(fun):
#     def test():
#         fun()
#         print(2)
#     return test
# @fun1
# def fun():
#     print(1)
# fun()
def power(fun):
    def wrap(*args,**kwargs):
        print('验证权限')
        return fun(*args,**kwargs)
    return wrap

@power
def enter_background():
    print('进入后台')
@power
def delete_order():
    print('删除订单')
enter_background()
delete_order()