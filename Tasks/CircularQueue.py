
class CircularQueue:
    def __init__(self, size):
        self.queue = [None] * size
        self.size = size
        self.front = -1
        self.rear = -1

    def enqueue(self, num):
        if (self.rear + 1) % self.size == self.front:
            print("Queue is full!")
            return self.queue

        if self.front == -1:
            self.front = 0

        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = num

        return self.queue

    def dequeue(self):
        if self.front == -1:
            print("Queue is empty!")
            return self.queue

        self.queue[self.front] = None

        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.size

        return self.queue

    def get_front(self):
        if self.front == -1:
            print("Queue is empty!")
            return None

        return self.queue[self.front]

    def get_rear(self):
        if self.rear == -1:
            print("Queue is empty!")
            return None

        return self.queue[self.rear]


size = int(input("Enter size of circular queue: "))
q = CircularQueue(size)

while True:
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Front")
    print("4. Rear")
    print("5. Exit")

    choice = input("Enter a number for operation: ")

    if choice == '1':
        num = int(input("Enter a number to enqueue: "))
        print(f"Queue after enqueue: {q.enqueue(num)} \n")

    elif choice == '2':
        print(f"Queue after dequeue: {q.dequeue()} \n")

    elif choice == '3':
        front_element = q.get_front()
        print(f"First element: {front_element} \n")

    elif choice == '4':
        rear_element = q.get_rear()
        print(f"Last element: {rear_element} \n")

    elif choice == '5':
        break

    else:
        print("Invalid choice. Try again! \n")
