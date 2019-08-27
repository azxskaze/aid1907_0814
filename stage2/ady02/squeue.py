from ady02.link_strack import StrackLink


class SQueueException(Exception):
    pass
class SQueue:
    def __init__(self):
        self._elems = []
    def is_empty(self):
        return self._elems == []
    def enqueue(self,val):
        self._elems.append(val)
    def pop(self):
        if self.is_empty():
            raise SQueueException
        return self._elems.pop(0)
    def top(self):
        return self._elems[0]
if __name__ == '__main__':
    aq1=SQueue()
    aq1.enqueue(3)
    aq1.enqueue(4)
    aq1.enqueue(1)
    aq1.enqueue(6)
    aq1.enqueue(5)
    aq1.enqueue(8)
    aq2=StrackLink()
    while aq1.is_empty() is not True:
        aq2.push(aq1.pop())
    while aq2.is_empty() is not True:

        aq1.enqueue(aq2.pop())
    while aq1.is_empty() is not True:
        print(aq1.pop())



