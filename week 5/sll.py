class Node:
    """Represents an individual node in the linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    """Manages the Singly Linked List and its operations."""
    def __init__(self):
        self.head = None

    # Display the linked list
    def display(self):
        if self.head is None:
            print("List is empty.")
            return

        current = self.head
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements) + " -> None")

    # 1. Insert at Beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        print(f"Inserted {data} at beginning.")

    # 2. Insert at End
    def insert_at_end(self, data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            print(f"Inserted {data} at end.")
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
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
            if current is None:
                print("Index out of bounds.")
                return
            current = current.next

        if current is None:
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
        self.head = self.head.next
        print(f"Deleted {deleted_val} from beginning.")

    # 5. Delete from End
    def delete_from_end(self):
        if self.head is None:
            print("List is empty. Nothing to delete.")
            return

        # If there's only one node
        if self.head.next is None:
            deleted_val = self.head.data
            self.head = None
            print(f"Deleted {deleted_val} from end.")
            return

        current = self.head
        while current.next.next:
            current = current.next

        deleted_val = current.next.data
        current.next = None
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
            if current.next is None:
                print("Index out of bounds.")
                return
            current = current.next

        if current.next is None:
            print("Index out of bounds.")
            return

        deleted_val = current.next.data
        current.next = current.next.next
        print(f"Deleted {deleted_val} from index {index}.")


# Example Usage / Driver Code
if __name__ == "__main__":
    sll = SinglyLinkedList()

    # Insertions
    sll.insert_at_beginning(20)
    sll.insert_at_beginning(10)
    sll.insert_at_end(40)
    sll.insert_at_index(30, 2)  # Inserts 30 at index 2

    # Display current list: 10 -> 20 -> 30 -> 40 -> None
    sll.display()

    # Deletions
    sll.delete_from_beginning()  # Deletes 10
    sll.display()

    sll.delete_from_end()        # Deletes 40
    sll.display()

    sll.delete_at_index(1)       # Deletes element at index 1 (which is 30)
    sll.display()