from threading import Thread,Lock
import time

#账户类
class Account:
    def __init__(self, id=None, blance=None, lock=None):
        self.id = id
        self.blance = blance
        self.lock = lock
    # 取钱
    def withdtaw(self,amount):
        self.blance -= amount
    # 存钱
    def deposit(self,amount):
        self.blance += amount
    def get_balance(self):
        return self.blance
alic = Account('alic',12000,Lock())

bob = Account('bob',9000,Lock())
# 转账 账户金额变动需要先上锁
def transfer(from_,to,amount):
    """

    :param from_: 付款方
    :param to: 收款方
    :param amount: 金额
    """
    if from_.lock.acquire():
        from_.withdtaw(amount)
        time.sleep(0.2)
        if to.lock.acquire():
            to.deposit(amount)
            to.lock.release()
        from_.lock.release()
    print('%s给%s转了%d元'%(from_.id,to.id,amount))

t1 = Thread(target=transfer,args=(alic,bob,3000))
t2 = Thread(target=transfer,args=(bob,alic,5000))
t1.start()
t2.start()
t1.join()
t2.join()
print('alic:',alic.blance)
print('bob:',bob.blance)