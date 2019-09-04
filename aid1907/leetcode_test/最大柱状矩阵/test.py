def max_j(heights):
    list1=[]
    for i in range(len(heights)):
        if heights[i] == 0:
            list1.append(0)
            continue
        min=heights[i]

        for j in range(i, len(heights)):
            if heights[j] == 0:
                j-=1
                break
            if heights[j]<min:
                min = heights[j]
        list1.append((j-i+1)*min)

    if list1 == []:
        return 0
    return max(list1)
def max_i(heights):
    list1=[]
    for i in range(len(heights)):
        if heights[i] == 0:
            list1.append(0)
            continue

        for j in range(i, len(heights)):

            if heights[j] < heights[i]:
                j-=1
                break
        # print(j,(j-i+1)*heights[i])

        list1.append((j-i+1) * heights[i])

    if list1 == []:
        return 0
    return max(list1)
def max_j1(heights):
    list1=[]
    for i in range(len(heights)):
        if heights[i] == 0:
            list1.append(0)
            continue
        min=heights[i]

        for j in range(i, len(heights)):
            if heights[j] == 0:
                j-=1
                break
            if heights[j]<min:
                min = heights[j]
        list1.append((j-i+1)*min)

    if list1 == []:
        return 0
    return max(list1)
def max_i1(heights):
    list1=[]
    for i in range(len(heights)):
        if heights[i] == 0:
            list1.append(0)
            continue

        for j in range(i, len(heights)):

            if heights[j] < heights[i]:
                j-=1
                break
        # print(j,(j-i+1)*heights[i])

        list1.append((j-i+1) * heights[i])

    if list1 == []:
        return 0
    print(list1)
    print(type(list1))
    return max(list1)
def maxl(heights):
    print(max_i(heights), max_j(heights),max_i1(heights), max_j1(heights))
    return  max(max_i(heights), max_j(heights),max_i1(heights), max_j1(heights))

print(max_j([[0,9]]))




