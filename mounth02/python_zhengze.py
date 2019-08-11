import re
line = "Cats aaaa1 ar2e s4ma5r6ter t3ha4n dogs"
pattern='\d'
# matchObj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)
# #
# # matchObj = re.match('www',line,re.M|re.I)
# print("matchObj.group(0) : ", matchObj)
# print("matchObj.group(1) : ", re.search(pattern,line).group())
# print("matchObj.group(2) : ", matchObj.group(2))
# print("matchObj.groups() : ", matchObj.groups())
print(re.findall(pattern,line))
