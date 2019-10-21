'''专门创建一个模块，用来进行版本管理，
可以对url进行版本定义和处理，
其他程序调用这个模块来对url进行统一管理'''
class UrlManager():
    @staticmethod
    def buildUrl(path):
        return path
    @staticmethod
    def buildStaticUrl(path):
        path += '?ver=' +'20190911400'
        return path