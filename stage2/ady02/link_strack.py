class Node:

    def __init__(self, val, next=None):
        self.val=val
        self.next=next

    def __str__(self):
        return '%s' % self.val
class StrackLink:
    def __init__(self):
        self._top=None
    def is_empty(self):
        return self._top  is  None
    def push(self,val):
        node=Node(val)
        node.next=self._top
        self._top=node
    def pop(self):
        temp=self._top
        self._top=self._top.next
        return temp
    def top(self):
        return self._top
if __name__=='__main__':
    s2=StrackLink()
    s2.push(2)
    s2.push(3)
    s2.push(4)
    s2.push(5)
    s2.push(9)
    s2.push(4)
    s2.pop()
    print(s2.top())
