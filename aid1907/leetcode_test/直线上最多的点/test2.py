
def maxPoints(points):
    def xy(a, b):
        if b[0] == a[0]:
            return
        k = (b[1] - a[1]) / (b[0] - a[0])
        b = a[1] - k * a[0]
        return (k, b)
    list2 = []
    if points == []:
        return 0
    for i in points:
        for j in range(len(points)):
            n = 0
            if points[j][0] == i[0]:
                continue
            else:
                k, b = xy(i, points[j])
                for m in range(len(points)):
                    if round(k * points[m][0] + b) == points[m][1]:
                        n += 1
            list2.append(n)

    list3 = []
    for i in points:
        n = 0
        for j in range(len(points)):
            if points[j][0] == i[0]:
                n += 1
        list3.append(n)
    if list2:
        a = max(list2)
    else:
        a = 1
    if list3:
        b = max(list3)
    else:
        b = 1

    return max(a, b)
list11 = [[560,248],[0,16],[30,250],[950,187],[630,277],[950,187],[-212,-268],[-287,-222],[53,37],[-280,-100],[-1,-14],[-5,4],[-35,-387],[-95,11],[-70,-13],[-700,-274],[-95,11],[-2,-33],[3,62],[-4,-47],[106,98],[-7,-65],[-8,-71],[-8,-147],[5,5],[-5,-90],[-420,-158],[-420,-158],[-350,-129],[-475,-53],[-4,-47],[-380,-37],[0,-24],[35,299],[-8,-71],[-2,-6],[8,25],[6,13],[-106,-146],[53,37],[-7,-128],[-5,-1],[-318,-390],[-15,-191],[-665,-85],[318,342],[7,138],[-570,-69],[-9,-4],[0,-9],[1,-7],[-51,23],[4,1],[-7,5],[-280,-100],[700,306],[0,-23],[-7,-4],[-246,-184],[350,161],[-424,-512],[35,299],[0,-24],[-140,-42],[-760,-101],[-9,-9],[140,74],[-285,-21],[-350,-129],[-6,9],[-630,-245],[700,306],[1,-17],[0,16],[-70,-13],[1,24],[-328,-260],[-34,26],[7,-5],[-371,-451],[-570,-69],[0,27],[-7,-65],[-9,-166],[-475,-53],[-68,20],[210,103],[700,306],[7,-6],[-3,-52],[-106,-146],[560,248],[10,6],[6,119],[0,2],[-41,6],[7,19],[30,250]]
c = maxPoints(list11)
print(c)