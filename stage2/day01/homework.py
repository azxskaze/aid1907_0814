'''单链表'''
import time


class Node:

    def __init__(self, val, next=None):
        self.val=val
        self.next=next

    def __str__(self):
        return '%s'%self.val
"""

1.构建节点关系
2.在节点中存储数据
3.对单链表进行节点操作

"""
class LinkList:
    '''
    生成对象表即单链表对象
    对象调用方法可以完成单链表的各种操作
    '''
    def __init__(self):
        '''初始化时 创建一个无用的节点
            让节点拥有该对象，以表达链表的开端
            '''
        self.head=Node(None)#头节点

    def add_node(self,args):
        p=self.head
        for i in args:
            p.next=Node(i)
            p=p.next


    def show(self):
        p=self.head.next
        while p:
            print(p.val)
            p=p.next
    def is_null(self):
        '''判断是否为空'''
        return not self.head.next
    def clear_node(self):
        self.head.next=None

    def append_node(self,iter):
        '''尾部插入数据'''
        p = self.head.next
        while p.next:
            p = p.next
        for i in iter:
            p.next = Node(i)
            p = p.next


    def insert_node(self,num,iter):
        '''插入节点'''
        p=self.head
        for i in range(num):
            if p.next is None:
                break
            p=p.next
            q=p.next
        # p.next=None
        for i in iter:
            p.next=Node(i)
            p=p.next
        p.next=q


    def delete_node_index(self,num):
        '''按位置删除'''
        p=self.head
        for i in range(num):
            if p.next is None:
                break
            p=p.next
        p.next=p.next.next



    def delete_node_val(self,value):
        '''按值删除'''
        p=self.head
        while p.next:
            if p.next.val==value:
                p.next=p.next.next
                break
            p=p.next
        else:
            print('不存在')

    def get_val(self,index):
        p=self.head
        for i in range(index+1):
            if p.next is None:
                raise  IndexError
            else:
                p = p.next

        print(p.val)

    def add_node_list(self,node_list):
        '''有序链表合并'''
        p=self.head
        q=node_list.head

        while q.next:
            b=0
            if q.next is None:
                break
            while p.next:
                if q.next.val>p.next.val and p.next.next == None:
                    p.next.next=q.next
                    break

                if p.next.val<=q.next.val and q.next.val<=p.next.next.val :
                    a=q.next
                    q.next=q.next.next
                    a.next=p.next.next
                    p.next.next=a
                    b=1
                    break
                p=p.next
            if b!=1:
                q=q.next





list1=LinkList()
list1.add_node(range(1,100,2))

list2=LinkList()
list2.add_node(range(2,100,2))

list1.add_node_list(list2)
list1.show()











