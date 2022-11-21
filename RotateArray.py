test_list = [1, 2, 3, 4, 5, 6]
k = 3

for i in range(k):
    test_list.insert(i , test_list.pop())


print(test_list)
