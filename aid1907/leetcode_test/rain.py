'''第一种方法超出时间限制'''
l=[1,2,1,2,5,4,6]
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        sum=0
        for i in range(1,len(height)-1):
            max_left = max_right = height[i]
            for j in range(i,-1,-1):
                if height[j] > max_left:
                    max_left = height[j]

            for k in range(i,len(height)):
                if height[k] > max_right:
                    max_right = height[k]

            if height[i] < min(max_left,max_right):
                sum += min(max_left,max_right)-height[i]

        return sum







