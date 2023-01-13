def findletters(t, s):
    list = []
    list2 = []
    splitT = [a for a in t]
    splitS = [b for b in s]
    position = 0
    count = 0
    count2 = 0
    #FirstList
    if len(splitT) > len(splitS):
        
        for i in splitS:
            
            if i in splitT:
                count += 1
                
            if count == len(splitS):
                for h in splitT:
                    if i in splitS:
                        position = splitT.index(i)
                        list = splitT[:position]
                        half = splitT[position + 1:]
                        
                   
                        break
            
        #secondlist    
        for j in splitS:
                
                if j in half:
                    count2 += 1
                    print(count)
                if count2 == len(splitS):
                    
                    for k in half:
                    
                        if k in splitS:
                            position2 = list.index(k)
                            list2 = half[position2:]
                            print(list2)
                          
                    
                            break
                            
        if len(list) >=  len(list2):
            print(list2)
        else: 
            print(list)
            
            
    #T Lower  
    if len(splitT) < len(splitS):
        print("Error")
    #T equals
    if  t == s :
        print(s)
    """if len(splitT) < len(splitS):
        for l in splitS:
            count = 0
            if l in splitT:
                count += 1
            if count == len(splitS):
                print("Boi")
            
                for m in splitT:
            
                    if m in splitS:
                        position = splitS.index(m)
                        newhalf = splitS[position + 1:]
                        newlist = splitS[:position]
                        print(list)
                        break
                
        
        
        for t in newhalf:
            if t in splitS:
                    count += 1
            if count == len(spliT):
                index = list.index(t)
                list2 = list[index:]
                print(list2)
                break
        print(newlist)
        if len(list) >  len(list2):
            print( list2 )
        else: 
            print(list)"""
        
findletters("a", "aa")            
