# import json
#
# l = [1,1,2,5]
# d = {'a':1,'b':2}
# # print(json.dumps(l))
# a = json.dumps(l)
# print(type(a),a)
# b = json.loads(a)
# print(b)
import re
l = 'GET / HTTP/1.1'
pattern = r"(?P<method>[A-Z]+)\s+(?P<info>/\S*)"
env = re.match(pattern, l).groupdict()
print(env)