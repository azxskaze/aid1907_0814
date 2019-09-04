
import itertools
class Solution:
    def findSubstring(self, s: str, words: list):
        list2=[]
        tmp_list = itertools.permutations(s)
        for i in tmp_list:
            str2=''.join(i)
            len1=len(str2)
            len2=len(words)
            for i in range(len2-len1):
                if words[i:len2].startswith(str2):
                    list2.append(i)
        return list2
str11="foobarman"
l=["foo","bar"]
# l=[1,3,5]
l1=Solution()
a=l1.findSubstring(["foo","bar"],"barfoothefoobarman")
print(a)