'''
替换空格
运行时间：24ms
占用内存：5624k
'''
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        if s=='':
            return ''
        return s.replace(' ','%20')