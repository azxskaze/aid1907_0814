class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        total_sum = 0
        if height == []:
            return 0
        d = height.index(max(height))
        def left(d):
            nonlocal total_sum
            l = height[:d]
            if l == []:
                return
            d1=l.index(max(l))
            del l
            sun=0
            for i in range(d1+1,d):
                sun+=height[i]
            total_sum+=((d-d1-1)*min(height[d1],height[d])-sun)
            left(d1)

        def right(d):
            nonlocal total_sum
            l=height[d+1:len(height)]
            if l == []:
                return
            d1=d+1+l.index(max(l))
            del l
            sun=0
            for i in range(d+1,d1):
                sun+=height[i]
            total_sum+=((d1-d-1)*min(height[d1],height[d])-sun)
            right(d1)
        left(d)
        right(d)
        return total_sum



t=Solution()
l=[3,2,6,1,6,6,2,6,1,6,6,2,6,1,6]
print(t.trap(l))