# from day01.model import Node
# from day01.model import LinkList
class Node:

    def __init__(self, val, next=None):
        self.val=val
        self.next=next

    def __str__(self):
        return '%s'%self.val

class StrackError(Exception):
    pass
class Strack:
    def __init__(self):
        self.strack=Node(None)
    def is_null(self):
        return self.strack.next == None
    def push(self,val):
        node=Node(val)
        if self.strack.next:
            node.next=self.strack.next
        self.strack.next=node
    def pop(self):
        if self.is_null():
            raise StrackError
        a=self.strack.next
        if self.strack.next.next:
            self.strack.next=self.strack.next.next
        return a
    def top(self):
        if self.is_null():
            raise StrackError
        return self.strack.next.val
if __name__=='__main__':
    s2=Strack()
    s2.push(2)
    s2.push(3)
    s2.push(4)
    s2.push(5)
    s2.push(9)
    s2.pop()
    s2.pop()
    s2.pop()
    print(s2.top())