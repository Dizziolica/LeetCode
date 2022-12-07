def permutation(n, k, p):
    
    import random 
    lista = []
    result = 1
    lista3 = []
    permutation = []
    while  k > 1:
        result = k * result
        k = k - 1
    print( result)

    for i in range(1, n + 1):
         lista.append(i)
         print(lista)
    

        
    while len(permutation) < result:

         random.shuffle(lista)
         lista3 = lista.copy()
        
         print(lista3)
         if lista3 not in  permutation :
             permutation.append(lista3)
        
    
         

  
    
  
    print(permutation[4])
    print(permutation)
    
permutation(3, 3, 4)

        

