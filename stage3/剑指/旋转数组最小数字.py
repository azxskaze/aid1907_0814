# -*- coding:utf-8 -*-
'''运行时间：650ms
占用内存：5724k'''
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if rotateArray==[]:
            return 0
        a = min(rotateArray)
        return a
        # for i in range(len(rotateArray)):
        #     if rotateArray[i]==a:
        #         l1=rotateArray[i:len(rotateArray)]
        #         l2=rotateArray[0:i]
        #         l1.extend(l2)
        #         return l1
if __name__ == '__main__':
    s=Solution()
    a=s.minNumberInRotateArray([6501,6828,6963,7036,7422,7674,8146,8468,8704,8717,9170,9359,9719,9895,9896,9913,9962,154,293,334,492,1323,1479,1539,1727,1870,1943,2383,2392,2996,3282,3812,3903,4465,4605,4665,4772,4828,5142,5437,5448,5668,5706,5725,6300,6335])
    print(a)

