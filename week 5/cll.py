class Node:
    """Represents an individual node in the circular linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    """Manages the Circular Linked List operations."""
    def __init__(self):
        self.head = None

    # Display the linked list
    def display(self):
        if self.head is None:
            print("List is empty.")
            return

        elements = []
        current = self.head
        while True:
            elements.append(str(current.data))
            current = current.next
            if current == self.head:
                break
        
        print(" -> ".join(elements) + " -> (HEAD)")

    # 1. Insert at Beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            new_node.next = new_node
            self.head = new_node
        else:
            current = self.head
            # Traverse to the last node
            while current.next != self.head:
                current = current.next
            
            new_node.next = self.head
            current.next = new_node
            self.head = new_node

        print(f"Inserted {data} at beginning.")

    # 2. Insert at End
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            new_node.next = new_node
            self.head = new_node
        else:
            current = self.head
            # Traverse to the last node
            while current.next != self.head:
                current = current.next
            
            current.next = new_node
            new_node.next = self.head

        print(f"Inserted {data} at end.")

    # 3. Insert at Specific Index (0-based)
    def insert_at_index(self, data, index):
        if index < 0:
            print("Invalid index.")
            return

        if index == 0:
            self.insert_at_beginning(data)
            return

        new_node = Node(data)
        current = self.head

        for _ in range(index - 1):
            current = current.next
            if current == self.head:
                print("Index out of bounds.")
                return

        new_node.next = current.next
        current.next = new_node
        print(f"Inserted {data} at index {index}.")

    # 4. Delete from Beginning
    def delete_from_beginning(self):
        if self.head is None:
            print("List is empty. Nothing to delete.")
            return

        deleted_val = self.head.data

        # Single element in the list
        if self.head.next == self.head:
            self.head = None
        else:
            current = self.head
            # Find the last node to update its next pointer
            while current.next != self.head:
                current = current.next
            
            self.head = self.head.next
            current.next = self.head

        print(f"Deleted {deleted_val} from beginning.")

    # 5. Delete from End
    def delete_from_end(self):
        if self.head is None:
            print("List is empty. Nothing to delete.")
            return

        # Single element in the list
        if self.head.next == self.head:
            deleted_val = self.head.data
            self.head = None
            print(f"Deleted {deleted_val} from end.")
            return

        current = self.head
        # Traverse to second-to-last node
        while current.next.next != self.head:
            current = current.next

        deleted_val = current.next.data
        current.next = self.head
        print(f"Deleted {deleted_val} from end.")

    # 6. Delete from Specific Index (0-based)
    def delete_at_index(self, index):
        if self.head is None or index < 0:
            print("Invalid operation or list is empty.")
            return

        if index == 0:
            self.delete_from_beginning()
            return

        current = self.head
        for _ in range(index - 1):
            current = current.next
            if current.next == self.head:
                print("Index out of bounds.")
                return

        target = current.next
        if target == self.head:
            print("Index out of bounds.")
            return

        deleted_val = target.data
        current.next = target.next
        print(f"Deleted {deleted_val} from index {index}.")


# Example Usage / Driver Code
if __name__ == "__main__":
    cll = CircularLinkedList()

    # Insertions
    cll.insert_at_beginning(20)
    cll.insert_at_beginning(10)
    cll.insert_at_end(40)
    cll.insert_at_index(30, 2)  # Inserts 30 at index 2

    # Display List
    cll.display()

    # Deletions
    cll.delete_from_beginning()  # Deletes 10
    cll.display()

    cll.delete_from_end()        # Deletes 40
    cll.display()

    cll.delete_at_index(1)       # Deletes element at index 1 (which is 30)
    cll.display()