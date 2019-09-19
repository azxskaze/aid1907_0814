import json
f = open('static/4041.html')
data = json.dumps({'status':'200','data':f.read()})
print(type(data),data)
m = json.loads(data)
print(type(m))
