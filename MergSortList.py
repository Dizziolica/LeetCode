list = [1,2,3,0,0,0]
n = 3
list2 = [2,4,5]
listmerge = list + list2
newlist = []
for i in listmerge:
    if i == 0:
        continue
    else:
        newlist.append(i)
newlist.sort()
print(newlist)
