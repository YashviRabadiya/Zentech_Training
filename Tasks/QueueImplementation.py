def enqueue(arr, num):
	arr.append(num)
	return arr
	

def dequeue(arr):
	if not arr:
		print("Queue is empty!")
		return arr
	arr.pop(0)
	return arr

def peek(arr):
	if not arr:
		print("Queue is empty!")
		return None
	return arr[0]

stack = []

while True:
    print("1. enqueue")
    print("2. dequeue")
    print("3. Peek")
    print("4. Exit")

    choice = input("Enter a number for operation: ")

    if choice == '1':
        num = int(input("Enter a number to enqueuqe: "))
        print(f"Queue after enqueue: {enqueue(stack, num)} \n")
    elif choice == '2':
        print(f"Queue after dequeue: {dequeue(stack)} \n")
    elif choice == '3':
        top_element = peek(stack)
        print(f"First element : {top_element} \n")
    elif choice == '4':
        break
    else:
        print("Invalid choice.Try again! \n")  
	