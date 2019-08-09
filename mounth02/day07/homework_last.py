
def count_chr(str01):
    dict02 = {}
    for i in str01:
        if i not in dict02:
            dict02[i]=1
        else:
            dict02[i]+=1
    return dict02
str01 = 'this is a tese string'
print(count_chr(str01))
