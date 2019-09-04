def b(l:list,words,step,start,li,i):
    l2=l[:]
    # for j in range(start,len(words)):
    #     for item in l2:
    #         if words[j:len(words)].startswith(item):
    #             l2.remove(item)
    #             if l2 == []:
    #                 li.append(j+len(l[0]))
    #                 b(l,words,step-i,i,li,i)
    #             b(l2,words,step-len(l[0]),j+len(l[0]),li,i)
    # return list1
    for j in range(start,len(words)):
        for item in l2:
            if words[j:len(words)].startswith(item):
                l2.remove(item)
                if l2 == []:
                    li.append(i)
                    b(l2,words,step,j+len(l[0]),li,i)
                    return li
# def a(s:list,words):
#
#     l1=len(words)
#     l2=len(s)*len(s[0])
#     start=l1-l2
#     return b(s,words,start)
def a(l:list,words,step,start,li):
    for i in range(step):
        return b(l,words,step,start,li,i)
words="barfoothefoobarman"
l1=len(words)
s=["foo","bar"]
l2=len(s)*len(s[0])
step=l1-l2
star=0
list1=[]
a1=a(s,words,step,star,list1)

print(a1)
#
# print('12345'[1:-1].startswith('23'))