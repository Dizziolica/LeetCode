def swap(list1 , list2):
        count = 0
        copylist1 = [k for k in list1]
        for k in list1:
            if k in list2:
                count += 1
            if count == len(list2):
                for m in range(len(list1)):
                    
                    if list1[m] != list2[m]:
                        list1.remove(list1[m])
                        list1.insert(m, list2[m])
                        print(list1, list2)
               
swap([4,2,2,2],[1,4,1,2])
