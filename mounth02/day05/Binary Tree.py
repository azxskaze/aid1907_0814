# class Binary_Tree:
#     def __init__(self,data,lefft,right):
#         self.data = data
#         self.lefft = lefft
#         self.right = right

def create_Binary_Tree(array):
    level_tree=[]
    i=1
    for n in range(i):
        level_tree.append(array[i-1:i*2-1])
        i*=2
        if i>len(array):
            break

array=['a','b','c','d','e','f','g']






