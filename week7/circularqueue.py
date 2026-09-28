# Circular Queue Implementation

class CircularQueue:

    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1

    # Enqueue operation
    def enqueue(self, value):

        # Check if queue is full
        if (self.rear + 1) % self.size == self.front:
            print("Queue Overflow")
            return

        # First element
        if self.front == -1:
            self.front = 0
            self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.size

        self.queue[self.rear] = value
        print(value, "inserted into queue")

    # Dequeue operation
    def dequeue(self):

        # Check if queue is empty
        if self.front == -1:
            print("Queue Underflow")
            return

        value = self.queue[self.front]
        self.queue[self.front] = None

        # If only one element exists
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.size

        print(value, "deleted from queue")

    # Peek operation
    def peek(self):

        if self.front == -1:
            print("Queue is empty")
        else:
            print("Front element:", self.queue[self.front])

    # Display operation
    def display(self):

        if self.front == -1:
            print("Queue is empty")
            return

        print("Queue elements:", end=" ")

        i = self.front

        while True:
            print(self.queue[i], end=" ")

            if i == self.rear:
                break

            i = (i + 1) % self.size

        print()


# Main Program

size = int(input("Enter the size of circular queue: "))

cq = CircularQueue(size)

while True:

    print("\n========== CIRCULAR QUEUE MENU ==========")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        value = int(input("Enter value to enqueue: "))
        cq.enqueue(value)

    elif choice == 2:
        cq.dequeue()

    elif choice == 3:
        cq.peek()

    elif choice == 4:
        cq.display()

    elif choice == 5:
        print("Program exited.")
        break

    else:
        print("Invalid choice")