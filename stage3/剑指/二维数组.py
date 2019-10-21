'''
二维数组中的查找
运行时间：229ms
占用内存：5624k
'''
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code heres
        if array==[]:
            return False
        l = len(array[0])
        k=l
        for i in range(l):
            if array[i][0] > target:
                return False
            for j in range(l):
                if j>k:
                    return False
                if target < array[i][j]:
                    if j<k:
                        k=j
                    break
                if target==array[i][j]:
                    return True

