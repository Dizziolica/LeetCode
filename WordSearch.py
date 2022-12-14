
words = ["oath","pea","eat","rain"]
row1 = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
count = []

def verified2(list, word):
        
    wordsis = []
        
    lista = []
    listaword = []
        
    for m in row1:
        wordsis = wordsis + m
    
    for n in list:
            
        if n in wordsis:

            lista.append(n)
                
                
    finalword = "".join(lista)
    listaword.append(finalword)
    print(listaword)


def listafinal(finalword, listaword):

        listaword.append(finalword)
                    
        print(listaword)
       
          
def verified(word):
  
    list = []
    
    for j in word:
        
        list.append(j)
    
        
    verified2(list, word)
    
for i in range(len(words)):
    
 
    verified(words[i])
   
