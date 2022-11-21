s = "abcabcabcabc"
x = []
for i in s:
    if i not in x:
        x.append(i)
      
print(len(x))
