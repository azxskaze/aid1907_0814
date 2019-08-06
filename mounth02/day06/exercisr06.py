list_scor=[]
while True:
    scor=input('plz key scor:')
    if scor:
        list_scor.append(int(scor))
    else:
        break
print(max(list_scor),min(list_scor),sum(list_scor)/len(list_scor))

def int_str(i):
    return str(i)
def str_int(i):
    return int(i)
print(list(map(int_str,list_scor)))
print(list(map(str_int,list_scor)))
