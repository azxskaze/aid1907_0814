class SQueueException(Exception):
    pass
class Node:

    def __init__(self, val, next=None):
        self.val=val
        self.next=next

    def __str__(self):
        return '%s' % self.val
class LinkSqueue:
    def __init__(self):
        self._top=self._bottom=Node(None)
    def is_empty(self):
        return self._top is self._bottom
    def enqueue(self,val):
        node=Node(val)
        self._bottom.next=node
        self._bottom=node
    def pop(self):
        if self.is_empty():
            raise SQueueException
        temp=self._top.next
        self._top.next=self._top.next.next
        return temp
if __name__ == '__main__':
    s1=LinkSqueue()
    print(s1.is_empty())
    s1.enqueue(5)
    s1.enqueue(4)
    s1.enqueue(6)
    s1.enqueue(7)
    s1.enqueue(3)
    s1.enqueue(2)
    print(s1.pop())
    print(s1.pop())
    print(s1.pop())
    print(s1.pop())
    print(s1.is_empty())
