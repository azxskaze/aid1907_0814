'''自定义异常类'''
class AgeError(Exception):
    def __init__(self, message, code,id):
        # 错误信息
        self.message = message
        # 错误代码
        self.code = code
        # 错误编号
        self.id = id
class AtkError(Exception):
    def __init__(self, id,code,message,):
        # 错误信息
        self.message = message
        # 错误代码
        self.code = code
        # 错误编号
        self.id = id