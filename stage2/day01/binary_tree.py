class Node:
    def __init__(self,val=None,left=None,right=None):
        self.left=left
        self.right=right
        self.val=val


class BinaryTree:

    def __init__(self):

       self.node=Node()
    def full_create(self,iter):
        self.node=Node(iter[0])
        node=self.node
        for i in iter:
            def a(i):
                node.left = Node(i)

                node.right = Node(i)





    def left(self):
        res=[]
        root=self.node
        def preorderTraversal(root,res):
            res.append(root)
            preorderTraversal(root.left,res)
            preorderTraversal(root.right,res)
        return res





tree=BinaryTree()
tree.full_create('abcdef')
tree.left()

