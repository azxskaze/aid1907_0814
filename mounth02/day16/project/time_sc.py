'''时戳'''
import time
a=time.time()
# 获取当前时间戳（1970.1.1到现在的总秒）
print(time.localtime(a))
# 显示详细时间信息（元组）
# 将时戳传到localtime里面可以获取当时的时间
# 里面为空可以显示当前信息
time_tuple=time.localtime()
print(time.mktime(time_tuple))
# 将时间元祖变为时戳
print(time.strftime('%y/%m/%d %H:%M:%S',time_tuple))
# 将时间元组转换为时间字符串(固定格式)
print(time.strptime('19/08/21 11:31:60','%y/%m/%d %H:%M:%S'))
# 将时间字符串转换为时间元组(固定格式)