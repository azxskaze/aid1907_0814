def a(words:list, s):

    li=[]
    for i in range(step):
        # if b(words,s,i):
        b(words, s, i, li)
    return li


def b(l,words,i,li):
    l2 = l[:]
    global len2

    for item in l2:
        if words[i:len(words)].startswith(item):
            l2.remove(item)
            i+=len(l[0])
            if l2 == []:
                li.append(i-len2)
            b(l2,words,i,li)
    else:
        return False


s="barfoothefoobarman"
l1=len(s)
words=["foo","bar"]
len2=len(words)*len(words[0])
step=l1-len2
star=0
a1=a(words,s)
print(a1)