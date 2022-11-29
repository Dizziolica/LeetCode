def firstmini(height):

    min = []

    height.sort()

    res = height[1:]
    minimum = height[0]

    for i in height:
    
        for j in res:
      
       

            if i > 0:
                if i == minimum and j == i + 1:
                    height.remove(height[0])
                    min.append(i)
                    min.append(j)
    maximum = max(min)
    maximum += 1
    print(maximum)
