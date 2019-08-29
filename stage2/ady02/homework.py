from ady02.link_strack import StrackLink

'''判断括号是否正确'''
str1=')Open source (({soft]ware) }[is] made <better when {users} can easily (contribute] code and documentation to ' \
     'fix ' \
     'bugs and add features. ([Python strongly) encourages community {involvement in (improving) the software}. Learn more about how to make Python better for everyone.'
s1=StrackLink()
dict1={')':'(',']':'[','}':'{','>':'<'}
for i in range(len(str1)):
    if str1[i] in '({[<':
        s1.push((str1[i],i))
    elif str1[i] in')}]>':
        if s1.is_empty():
            print('error', str1[i], i)
        elif s1.top().val[0] == dict1[str1[i]]:
            s1.pop()
        else:
            print('error',str1[i],i)
while s1.is_empty() == False:
    a=s1.pop()
    print('error', a.val[0], a.val[1])
