from day02.squeue import SQueue


class Node:
    def __init__(self,val=None,left=None,right=None):
        self.left=left
        self.right=right
        self.val=val


class BinaryTree:

    def __init__(self):

       self.node=Node()
       self.sq1=SQueue()
    # def full_create(self,iter):
    #     self.node=Node(iter[0])
    #     node=self.node
    #     for i in iter:
    #         def a(i):
    #             node.left = Node(i)
    #
    #             node.right = Node(i)
    # str='abd##e##c##'
    def create_xianxu(self,str1):
        '''先序创建二叉树
        写递归的时候一定要注意操作的是什么类型的数据
        如果是可变数据容器
        就不需要考虑作用域，如果不可变就要声明局部变量或者全局变量'''
        def left():
            nonlocal i
            if str1[i] is None:
                return True
            elif str1[i] == '#':
                i+=1
            else:
                root = Node(str1[i])
                i += 1
                root.left= left()
                root.right= left()
                return root
        i=0
        self.node=left()



    def xianxu(self):
        '''先序遍历'''
        res=[]
        root=self.node
        def preorderTraversal(root,res):
            if root is None:
                return
            else:
                res.append(root)
                preorderTraversal(root.left,res)
                preorderTraversal(root.right,res)
        preorderTraversal(root,res)
        return res

    def left(self):
        '''中序遍历'''
        res=[]
        root=self.node
        def preorderTraversal(root,res):
            if root is None:
                pass
            else:
                preorderTraversal(root.left,res)
                res.append(root)
                preorderTraversal(root.right,res)
        preorderTraversal(root,res)
        return res

    def right(self):
        '''后序遍历'''
        res=[]
        root=self.node
        def preorderTraversal(root,res):
            if root is None:
                pass
            else:
                preorderTraversal(root.left,res)
                preorderTraversal(root.right,res)
                res.append(root)
        preorderTraversal(root,res)
        return res

    def cengcibianli(self):
        '''层序遍历，用队列实现
        进队根节点
        判断队列是否为空
        不为空，出队一个节点，再进队他的左右节点
        直到队列为空
        出队的顺序正好为层序遍历顺序'''
        root=self.node
        self.sq1.enqueue(root)
        while self.sq1.is_empty() is False:
            res=self.sq1.pop()
            if res.left:
                self.sq1.enqueue(res.left)
            if res.right:
                self.sq1.enqueue(res.right)
            print(res.val)








tree=BinaryTree()
# tree.node=Node('a')
# a=tree.node
# b=a.left=Node('b')
# c=a.right=Node('c')
# d=b.left=Node('d')
# e=b.right=Node('e')
# g=e.left=Node('g')
# f=c.right=Node('f')
# h=f.right=Node('h')
tree.create_xianxu('abd##e##c##')
tree.cengcibianli()
for i in tree.xianxu():
    print(i.val)

