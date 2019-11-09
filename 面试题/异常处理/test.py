from 面试题.异常处理.rizhi import logger

try:
    1 / 0
except:
    logger.error('发生了错误\n')

    # 等同于error级别，但是会额外记录当前抛出的异常堆栈信息，括号内可以提示哪个模块哪一行
    # logger.exception('this is an exception message,test.py,4行\n')
