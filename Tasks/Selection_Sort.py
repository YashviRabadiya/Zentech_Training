num = [64, 34, 25, 12, 22, 11, 90]

def selection_sort(arr):

    n = len(arr)

    for i in range(n):
        min = i
        for j in range(i + 1, n):
            if arr[j] < arr[min]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]

print("Array before sorting: ", num)
selection_sort(num)
print("Array after sorting: ", num)