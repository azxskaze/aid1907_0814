def print_juxing(hang,lie,char):
    """
    打印矩阵
    :param hang: 矩形行数
    :param lie: 矩形列数
    :param char: 填充字符
    """
    for i in range(hang):
        for j in range(lie):
            print(char,end='')
        print()
print_juxing(5,4,'*')