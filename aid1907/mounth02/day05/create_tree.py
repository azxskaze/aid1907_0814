from Binary_Tree_copy import BTree

# 构造二叉树, BOTTOM-UP METHOD
right_tree = BTree(6)
right_tree.left = BTree(2)
right_tree.right = BTree(4)

left_tree = BTree(5)
left_tree.left = BTree(1)
left_tree.right = BTree(3)

tree = BTree(11)
tree.left = left_tree
tree.right = right_tree

left_tree = BTree(7)
left_tree.left = BTree(3)
left_tree.right = BTree(4)

right_tree = tree # 增加新的变量
tree = BTree(18)
tree.left = left_tree
tree.right = right_tree

print('先序遍历为:')
tree.preorder()
print()

print('中序遍历为:')
tree.inorder()
print()

print('后序遍历为:')
tree.postorder()
print()

print('层序遍历为:')
level_order = tree.levelorder()
print(level_order)
print()

height = tree.height()
print('树的高度为%s.' % height)

print('叶子节点为：')
tree.leaves()
print()

# 利用Graphviz进行二叉树的可视化
tree.print_tree(save_path='E://BTree.gv', label=True)