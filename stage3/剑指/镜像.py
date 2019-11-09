# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):

        def left(root):
            if not root:
                return
            node = root.right
            root.right = root.left
            root.left = node
            left(root.left)
            left(root.right)
        left(root)
        return root