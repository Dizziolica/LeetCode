def Container(list):
    maxnum1, maxnum2 =  0, 0
    newlist2 = []

    for i in list:
    
        if i > maxnum1:
            maxnum1 = i
      
        else:
            continue



    newlist2.append(maxnum1)
    newlist = list.copy()
    newlist.remove(maxnum1)
    maxnum2 = max(newlist)
    newlist2.append(maxnum2)

    result = min(newlist2)  *  (list.index(maxnum2)  - list.index(maxnum1))




    print(result)
    
Cointainer()
