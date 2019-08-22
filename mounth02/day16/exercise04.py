tuple01 = (1,5,26,54,5,26,85)
tupleiter = tuple01.__iter__()
while True:
    try:
        print(tupleiter.__next__())
    except StopIteration:
        print('meile')
        break

dict01 = {'张翠山':101,'殷素素':102,'张无忌':103}
dictiter=dict01.__iter__()
while True:
    try:
        a=dictiter.__next__()
        print(a,dict01[a])
    except StopIteration:
        print('meile')
        break