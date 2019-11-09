old =[{'id':1,'p':0},
      {'id':2,'p':1},
      {'id':3,'p':1},
      {'id':4,'p':3},]
new = []
for i in old:
    if i['p'] == 0:
        continue
    for j in new:
        if i['p'] == j['id']:
            j['childern'].append({'id':i['id']})
            break
    else:
        new.append({'id': i['p'], 'childern': [{'id': i['id']}]})
print(new)
# d = {}
# d.setdefault('k',[])