import re
# str1 = '456156@nfji.com,4568756@n8ji.com'
# re1 = r'\w+@\w+\.com'

# str1 = 'fds456_ik8'
# re1 = '[0-9a-z|_]{8,12}'

# str1 = '45,1.6,-85,75%,9/7'
# re1 = r'-?\d+\.?\/?\d+\%?'

str1 = 'Adfsjif,UHGJsad,iPython'
re1 = r'\b[A-Z]\w+'

a = re.findall(re1,str1)
print(a)



