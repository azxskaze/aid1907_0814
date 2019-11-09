# 也是变种的斐波那契数列

class Solution:
    def rectCover(self, number):
        res = [0,1,2]
        if number<3:
            return res[number-1]
        for i in range(number-2):
            res.append(res[i+1]+res[i+2])
        return res[number]
s = Solution()
print(s.rectCover(4))