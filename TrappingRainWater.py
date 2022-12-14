def RainWater(heightList):

result = 0
newlist = []
for i in range(len(heighListt)):
    

    if result < heightList[i] and result != heightList[i]:
        result = heightList[i] - result
       
    if result > heightList[i]  and result != heightList[i]:
        result = result - heighList[i]
    if heightList[i] == result:
        continue
    newlist.append(result)

print(sum(newlist))
