ef combination(s, p):
    count = 0
    
   
            
    if len(s) == len(p):
        for i in s:
            for j in p:
                
                if i == "?" or j == "?":
                    i = j 
                    j = i
                    count += 1
               
                if i == p:
                    count += 1 
                    
    if "*" in s or p:
        
            p = s
            s = p
            
            count = len(s)
            
            
    
            
                    
    if  count == len(s):
        
        print("True")
    
  
    else:
        print("False")
    
combination("aa", "?a")
