arr = [1,5,2,3,0,4]
rearranged = [0] * len(arr)
for i in range(len(arr)):
    rearranged[arr[i]] = i

print(rearranged)

