def rightmin(nums):
    list = []
    sortlist = sorted(nums)
    twominimo = sortlist[0:2]
    i = 0
    while i < len(nums):
        
        
        print(i)
        if i == nums[-1]:
            list.append(0)
            print(list)
            break
        
        if twominimo[0] in nums[i+1:] and twominimo[1] in nums[i+1:]:
            list.append(2)
            
        if twominimo[0] in nums[i+1:] or twominimo[1] in nums[i+1:]:
            list.append(1)
        
        
        
                
        
        i += 1    
           
    
    
rightmin([5,2,6,1])
