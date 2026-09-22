class Stack:
    """Simulates a Stack using a fixed-size array."""
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack = []  # Array to store stack elements
    
    # Helper method to check if the stack is empty
    def is_empty(self):
        return len(self.stack) == 0
    
    # Helper method to check if the stack is full
    def is_full(self):
        return len(self.stack) == self.capacity

    # 1. Push Operation (Insert element at the top)
    def push(self, data):
        if self.is_full():
            print(f"Stack Overflow! Cannot push {data}. Stack is full.")
            return
        
        self.stack.append(data)
        print(f"Pushed {data} to the stack.")

    # 2. Pop Operation (Remove and return the top element)
    def pop(self):
        if self.is_empty():
            print("Stack Underflow! Cannot pop. Stack is empty.")
            return None
        
        popped_item = self.stack.pop()
        print(f"Popped {popped_item} from the stack.")
        return popped_item

    # 3. Peek Operation (Return the top element without removing it)
    def peek(self):
        if self.is_empty():
            print("Stack is empty. Nothing to peek.")
            return None
        
        top_item = self.stack[-1]
        return top_item

    # 4. Display Operation (Print all elements from top to bottom)
    def display(self):
        if self.is_empty():
            print("Stack is empty.")
            return
        
        print("Stack elements (Top to Bottom):")
        # Loop backwards from the last index to 0
        for i in range(len(self.stack) - 1, -1, -1):
            print(f"| {self.stack[i]:^4} |")
        print("-------")


# Example Usage / Driver Code
if __name__ == "__main__":
    # Create a stack of capacity 5
    s = Stack(5)

    # Push operations
    s.push(10)
    s.push(20)
    s.push(30)
    s.push(40)
    
    # Display the stack
    s.display()
    
    # Peek operation
    print(f"\nTop element is: {s.peek()}\n")
    
    # Pop operations
    s.pop()
    s.pop()
    
    # Display after popping
    s.display()
    
    # Triggering Stack Overflow
    s.push(50)
    s.push(60)
    s.push(70)
    s.push(80) # This will cause an overflow since capacity is 5