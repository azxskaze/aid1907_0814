# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        if listNode == {}:
            return []
        list0 = []
        for i in listNode:
            list0.append(i)
        list2=list0[::-1]
        return list2


        # if listNode.next==None:
        #     return []
        # p = listNode
        # l=0
        # list1 = []
        # while p.next:
        #     list1.append(p.val)
        #     p=p.next
        #     l+=1
        # q = ListNode(list1.pop())
        # p = q
        # for i in range(-len(list1)-1,-1,-1):
        #     node = ListNode(list1[i])
        #     p.next = node
        #     p.next.next = p
        # return q

a = Solution()
print(a.printListFromTailToHead({1,2,3}))