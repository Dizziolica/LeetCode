
words = ["oath","pea","eat","rain"]
row1 = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]



count = []

def verified2(list, word):
        
        wordsis = []
        
        lista = []
        
        for m in row1:
            wordsis = m + wordsis
            
        
         
        for n in list:
            
            if n in wordsis:
                
                
                if len(lista) < len(word):
                    
                
                    lista.append(n)
                    
                if len(lista) > len(word) or len(lista) == len(word):
                    count.append(n)
        print(count) 
        print(lista)   
                
          
def verified(word):
  
    list = []
    
    for j in word:
        
        
        
        list.append(j)
    
        
    verified2(list, word)
    

        

        
        
            
for i in range(len(words)):
    
 
    verified(words[i])
