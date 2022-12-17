nums = [-1, 0, 1 ,2, -1, -4]
newlist1 = []
newlist2 = []
n = len(nums)

for i in range(n):
    for j in range(1, n):
        for k in range (2, n):
            
            if nums[i] + nums[j] +  nums[k] == 0:
                newlist1.append(nums[i])
                newlist1.append(nums[j])
                newlist1.append(nums[k])
print(newlist1)
