# 二叉树重构
class Node:
    def __init__(self,value=None,left=None,right=None):
        self.value=value
        self.left = left
        self.right=right

def tree(list1,list2):
    list1=list(list1)
    list2=list(list2)
    if not list1:
        return None
    node = Node(list1[0])
    print(list1,list2)
    i = list2.index(list1[0])
    node.left=tree(list1[1:i+1],list2[0:i])
    node.right=tree(list1[i+1:],list2[i+1:])
    return node

def reConstructBinaryTree(self, pre, tin):
    list1 = list(pre)
    list2 = list(tin)
    if not list1:
        return None
    node = Node(list1[0])
    print(list1, list2)
    i = list2.index(list1[0])
    node.left = reConstructBinaryTree(list1[1:i + 1], list2[0:i])
    node.right = reConstructBinaryTree(list1[i + 1:], list2[i + 1:])
    return node

def xianxu(root):
    res = []
    def preorderTraversal(root, res):
        if root is None:
            return
        else:
            print(type(root),root)
            res.append(root.value)
            preorderTraversal(root.left, res)
            preorderTraversal(root.right, res)

    preorderTraversal(root, res)
    return res
node = tree([1,2,4,7,3,5,6,8],[4,7,2,1,5,3,8,6])
print(node.left)
res = xianxu(node)
for i in res:
    print(i.value)
