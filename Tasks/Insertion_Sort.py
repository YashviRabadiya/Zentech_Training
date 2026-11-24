def insertionsort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# num = [64, 34, 25, 12, 22, 11, 90]

# print("Array before sorting: ", num)
# insertionsort(num)
# print("Array after sorting: ", num)