class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        sum=0
        for i in range(1,len(height)):
            max=0
            max_j=i-1
            for j in range(i-1,-1,-1):
                if max>=height[i]:

                    break
                if height[j]>max:
                    max=height[j]
                    max_j=j

            a=min(height[i],max)
            sun=0
            for item in range(max_j+1,i):
                sun+=height[item]
            sum+=(a*(i-max_j-1)-sun)
            for item in range(max_j+1,i):
                height[item]+=1

        return sum
s1=Solution()
print(s1.trap([4,2,0,3,2,5]))



