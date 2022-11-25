numletter = {"1": ["a","b", "c"], "2": ["d","e","f"], "3": ["g","h","i"], "4":["j","k","l"], "5":["m","n", "o"], "6":["p","q","r"], "7":["s","t","u"], "8":["w","v","x"] ,"9":["y", "z"]}
number = 23
strnumber = str(number)
result = 0
list = []
for i in numletter[strnumber[0]]:
    for j in  numletter[strnumber[1]]:
        result = i + j
        list.append(result)
        print(result)
        
        

print(result)
print(list)
