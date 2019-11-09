class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # 如果输入的不是矩阵需要手动转换成正方形
        # write code here
        # l = len(matrix)
        # num = int(l**0.5)
        # print(num)
        # res = []
        # for i in range(num):
        #     list1 = []
        #     for j in range(num):
        #         list1.append(matrix[i*num+j])
        #     res.append(list1)
        # print(res)
        num=len(matrix)
        num2 = len(matrix[0])
        a = 0
        b = num2-1
        c = num-1
        d = 0
        list1=[]
        while True:
            print(a,b,c,d)
            if d>b:
                break
            for i in range(d,b+1):
                list1.append(matrix[a][i])
            a+=1
            print(a,b,c,d)

            if a>c:
                break
            for i in range(a,c+1):
                list1.append(matrix[i][b])
            b-=1
            print(a,b,c,d)

            if b<d:
                break
            for i in range(b,d-1,-1):
                list1.append(matrix[c][i])
            c-=1
            print(a,b,c,d)

            if c<a:
                break
            for i in range(c,a-1,-1):
                list1.append(matrix[i][d])
            d+=1
        return list1


s = Solution()
a = s.printMatrix([1,2,3,4,5,6,7,8,9])
print(a)
# 1  2  3  4
# 5  6  7  8
# 9  10 11 12
# 13 14 15 16
#
# 0  a(d-b) a+=1 1 a(d-b) a+=1 2
# 3  b(a-c) b-=1 2 b(a-c) b-=1 2
# 3  c(b-d) c-=1 2 c(b-d) c-=1 2
# 0  d(c-a) d+=1 1 d(c-a) break
# 123
# 456
# 789
# 0220
# 1220
# 1120
# 1110