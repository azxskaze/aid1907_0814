class Solution:
    def isNumber(self,s):
        if s=='':
            return False
        listc=['.','-','+','e']
        list1=[]
        list2=[]
        list3=[]
        s=s.strip()
        for i in s:
            if i in listc:
                if i == 'e':
                    str1 = ''.join(list3)
                    print(list1)
                    list3.clear()
                else:
                    list3.append(i)
            else:
                try:
                    i=int(i)
                except:
                    return False
                i=str(i)
                list3.append(i)
                list2=list3
                str2=''.join(list2)
        if str1=='':
            return False


if __name__ == '__main__':
    s=Solution()
    s.isNumber('-996e88')

