class Node:

    def __init__(self, val, next=None, last=None):
        self.val=val
        self.next=next
        self.last=last

    def __str__(self):
        return '%s'%self.val

class LinkList:
    '''
    生成对象表即单链表对象
    对象调用方法可以完成单链表的各种操作
    '''
    def __init__(self):
        '''初始化时 创建一个无用的节点
            让节点拥有该对象，以表达链表的开端
            '''
        self.head=self.bottom=Node(None)
    def is_null(self):
        '''判断是否为空'''
        return  self.head == self.bottom
    def add_node(self,iter):
        for val in iter:
            node=Node(val)
            if self.is_null():
                self.head.next = node
                node.last = self.head
                self.bottom = node
            else:
                self.bottom.next = node
                node.last = self.bottom
                self.bottom = node
    def show1(self):
        p=self.head.next
        while p:
            print(p.val)
            p=p.next
    def show2(self):
        p=self.bottom
        while p != self.head:
            print(p.val)
            p=p.last

    def clear_node(self):
        self.head.next = None
        self.bottom.last = None

    def append_node(self,iter):
        '''尾部插入数据'''
        node = Node(iter)
        self.bottom.next = node
        node.last = self.bottom
        self.bottom = node


    def insert_node(self,num,val):
        '''插入节点'''
        p=self.head
        for i in range(num):
            if p.next is None:
                break
            p=p.next
            q=p.next


        node=Node(val)
        node.next=q
        q.last=node
        p.next=node
        node.last=p

    def delete_node_index(self,num):
        '''按位置删除'''
        p=self.head
        for i in range(num):
            if p.next is None:
                break
            p=p.next
        p.next=p.next.next
        p.next.next.last=p

    def delete_node_val(self,value):
        '''按值删除'''
        p=self.head
        while p.next:
            if p.next.val==value:
                p.next=p.next.next
                p.next.next.last=p
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
s=LinkList()
s.add_node((1,5,6,9,8,7))
s.insert_node(3,3)
s.delete_node_index(3)

s.show1()
s.show2()