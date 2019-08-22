#!/usr/bin/env python3
import sys
# # python的位置参数
print(sys.argv)
#
def add_student (name,id):
    print(name,id)
add_student(sys.argv[1],sys.argv[2])
print()
# '''在终端不用python3来执行python文件
# chmod +x add_student.py
# '+x'表示可以自动执行'''