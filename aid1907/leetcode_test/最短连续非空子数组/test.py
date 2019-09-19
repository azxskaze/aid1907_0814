'''求解最短非空连续组数组
示例 1：
输入：A = [1], K = 1
输出：1
示例 2：
输入：A = [1,2], K = 4
输出：-1
示例 3：
输入：A = [2,-1,2], K = 3
输出：3
提示：
1 <= A.length <= 50000
-10 ^ 5 <= A[i] <= 10 ^ 5
1 <= K <= 10 ^ 9
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shortest-subarray-with-sum-at-least-k
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''
def fun(A,K):
    l = len(A)
    max1 = 0
    for i in range(l):

        for j in range(i,l):
            sum = 0
            for n in range(i,j+1):
                sum += A[n]
                if sum >= K:

                    a = (n-i+1)
                    if  a > max1:
                        max1 = a
    if max1:
        return max1
    else:
        return -1
print(fun([2,-1,2],3))

