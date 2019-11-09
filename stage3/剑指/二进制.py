class Solution:
    def NumberOf1(self, n):
        c= 0
        if n<0:
            n = ~n
            print(n)
        while(n!=0):
            c+=1
            n=n&(n-1)
        return c
s = Solution()
print(s.NumberOf1(-5))