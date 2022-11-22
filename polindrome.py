s = 121
stris = str(s)
reverse = ""
number = len(stris)
confirm = True
for i in range(number):
    reverse += stris[i]
    print(reverse)


if stris == reverse:
    print(confirm)
else:
    confirm = False
    print("It is False")

