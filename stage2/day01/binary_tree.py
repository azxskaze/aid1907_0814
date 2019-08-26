class Node:
    def __init__(self,val=None,left=None,right=None):
        self.left=left
        self.right=right
        self.val=val

class BinaryTree:
    def __init__(self):
       pass

    def full_create(self,iter):
        count=1
        node=Node(iter[0])
        for i in range(1,len(iter),count*2):
            node.left=Node(iter[i])

            node.right=Node(iter[i+1])




