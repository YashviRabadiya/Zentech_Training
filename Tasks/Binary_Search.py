from Insertion_Sort import insertionsort

def binary_search(arr, target):

    insertionsort(arr)

    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

num = [11, 12, 22, 25, 34, 64, 90]
target = input("Enter a number to search: ")

result = binary_search(num, int(target))

if result != -1:
    print(f"Element found at index: {result}")
else:
    print("Element not found in the array.")
