def push(arr, num):
	arr.append(num)
	return arr

def pop(arr):		
	return arr.pop() if arr else print("Stack is empty")
    

def peek(arr):
	if not arr:
		print("Stack is empty")
		return None
	return arr[-1]

stack = []

while True:
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Exit")

    choice = input("Enter a number for operation: ")

    if choice == '1':
        num = int(input("Enter a number to push: "))
        print(f"Stack after push: {push(stack, num)} \n")
    elif choice == '2':
        print(f"Stack after pop: {pop(stack)} \n")
    elif choice == '3':
        top_element = peek(stack)
        print(f"Top element is: {top_element} \n")
    elif choice == '4':
        break
    else:
        print("Invalid choice.Try again! \n")  
	