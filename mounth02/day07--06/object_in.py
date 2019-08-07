def sum(a,b):
    return a+b

'''if __name__=='__main__':
相当于是C和JAVA中的void main()函数
也就是程序入口
文件再被当成模块导入，后面的主函数将不被执行'''

if __name__=='__main__':
    '''-->程序入口'''
    print(sum(1,2))

'''java'''
# public class add{
# public static void main(String args[]):——>程序入口
# {
# system.out.println(sum(1,2),%d)}}
'''c语言'''
# #include<stdio.h>
#  void main()  ——>程序入口
# {
#     printf(sum(1,2),%d)
# }

