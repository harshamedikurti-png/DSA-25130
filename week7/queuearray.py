# Queue Implementation using Array

class Queue:
    def __init__(self, size):
        self.queue = []
        self.size = size

    # Enqueue operation
    def enqueue(self, value):
        if len(self.queue) == self.size:
            print("Queue Overflow")
        else:
            self.queue.append(value)
            print(value, "inserted into queue")

    # Dequeue operation
    def dequeue(self):
        if len(self.queue) == 0:
            print("Queue Underflow")
        else:
            value = self.queue.pop(0)
            print(value, "deleted from queue")

    # Peek operation
    def peek(self):
        if len(self.queue) == 0:
            print("Queue is empty")
        else:
            print("Front element:", self.queue[0])

    # Display operation
    def display(self):
        if len(self.queue) == 0:
            print("Queue is empty")
        else:
            print("Queue elements:", end=" ")

            for value in self.queue:
                print(value, end=" ")

            print()


# Main Program

size = int(input("Enter the size of queue: "))

q = Queue(size)

while True:

    print("\n========== QUEUE MENU ==========")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        value = int(input("Enter value to enqueue: "))
        q.enqueue(value)

    elif choice == 2:
        q.dequeue()

    elif choice == 3:
        q.peek()

    elif choice == 4:
        q.display()

    elif choice == 5:
        print("Program exited.")
        break

    else:
        print("Invalid choice")