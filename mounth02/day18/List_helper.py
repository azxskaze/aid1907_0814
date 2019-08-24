'''
定义项目中所有对容器的操作
'''
class ListHelper:
    '''工具类'''
    '''静态方法，第一个参数是形参，而不是
    实例方法的（self）或者类方法的（cls）
    静态方法无法访问类变量和实例变量    
    调用（类名.方法）
    '''
    @staticmethod
    def find_single(iterable_target, func_condition):
        """

        :param iterable_target:
        :param func_condition:
        """
        for i in iterable_target:
            if func_condition(i):
                return i

    @staticmethod
    def find_all(iterable_target, func_condition):
        """

        :param iterable_target:
        :param func_condition:
        """
        for i in iterable_target:

            yield func_condition(i)
    @staticmethod
    def find_sum(iterable_target,func_condition):
        """
        按照条件求和
        :param iterable_target: 列表
        :param func_condition: 条件
        :return: 和
        """
        sum=0
        for i in iterable_target:
            sum+=func_condition(i)
        return sum

    @staticmethod
    def find_max(iterable_target, func_condition):
        """
        按照条件求最大值
        :param iterable_target: 列表
        :param func_condition: 条件
        :return: 最大值（int）
        """
        max_value=iterable_target[0]
        for i in range(1, len(iterable_target) - 1):
            if func_condition(iterable_target[i]) > func_condition(max_value):
               max_value=iterable_target[i]
        return max_value

    @staticmethod
    def find_min(iterable_target, func_condition):
        min_value = iterable_target[0]
        for i in range(1, len(iterable_target) - 1):
            if func_condition(iterable_target[i]) < func_condition(min_value):
                min_value = iterable_target[i]
        return min_value

    @staticmethod
    def ascending_order(iterable_target, func_condition):
        for i in range(len(iterable_target)-1):
            for j in range(len(iterable_target)-1-i):
                if func_condition(iterable_target[j])>func_condition(iterable_target[j+1]):
                    iterable_target[j+1],iterable_target[j]=iterable_target[j],iterable_target[j+1]

    @staticmethod
    def descending_order(iterable_target, func_condition):
        for i in range(len(iterable_target) - 1):
            for j in range(len(iterable_target) - 1 - i):
                if func_condition(iterable_target[j]) < func_condition(iterable_target[j + 1]):
                    iterable_target[j + 1], iterable_target[j] = iterable_target[j], iterable_target[j + 1]

    @staticmethod
    def delete_obj(iterable_target, func_condition,j):

        for i in range(len(iterable_target) - 1,-1,-1):
            if func_condition(iterable_target[i]) < j:
                del iterable_target[i]
