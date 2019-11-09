class Solution:

    a = 0
    def jumpFloor(self, number):
        def jump(number):
            if number<=1:
                Solution.a+=1
                return True
            jump(number-1)
            jump(number-2)
        jump(number)
        return Solution.a
s = Solution()
a = s.jumpFloor(10)
print(a)
# a=0
# def jump(number):
#     if number <= 1:
#         global a
#         a+=1
#         return True
#     jump(number-1)
#     jump(number-2)
# jump(3)
# print(a)
# 1 1 2 3 5 8 13 21 34 55 89
#   1 1 2 4 8
def fb(num):
    res = [1,1]
    for i in range(num-1):
        res.append(res[i]+res[i+1])
    return res[num]
print(fb(10))
class Solution:
    def jumpFloor(self, number):
        res = [1, 1]
        for i in range(number - 1):
            res.append(res[i] + res[i + 1])
        return res[number]

# 变态跳台阶
class Solution:
    def jumpFloor(self, number):
        res = [1, 1]
        for i in range(number - 1):
            res.append(sum(res))
        return res[number]