class Node:
    """Represents a node in a doubly linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    """Manages the Doubly Linked List operations."""
    def __init__(self):
        self.head = None

    # Display the list from head to end (Forward)
    def display_forward(self):
        if self.head is None:
            print("List is empty.")
            return

        current = self.head
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        print("None <-> " + " <-> ".join(elements) + " <-> None")

    # Display the list from end to head (Backward)
    def display_backward(self):
        if self.head is None:
            print("List is empty.")
            return

        current = self.head
        while current.next:
            current = current.next

        elements = []
        while current:
            elements.append(str(current.data))
            current = current.prev
        print("None <-> " + " <-> ".join(elements) + " <-> None")

    # 1. Insert at Beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is not None:
            self.head.prev = new_node
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
        new_node.prev = current
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
        new_node.prev = current

        if current.next is not None:
            current.next.prev = new_node

        current.next = new_node
        print(f"Inserted {data} at index {index}.")

    # 4. Delete from Beginning
    def delete_from_beginning(self):
        if self.head is None:
            print("List is empty. Nothing to delete.")
            return

        deleted_val = self.head.data
        self.head = self.head.next

        if self.head is not None:
            self.head.prev = None

        print(f"Deleted {deleted_val} from beginning.")

    # 5. Delete from End
    def delete_from_end(self):
        if self.head is None:
            print("List is empty. Nothing to delete.")
            return

        # If only one element exists
        if self.head.next is None:
            deleted_val = self.head.data
            self.head = None
            print(f"Deleted {deleted_val} from end.")
            return

        current = self.head
        while current.next:
            current = current.next

        deleted_val = current.data
        current.prev.next = None
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
        for _ in range(index):
            if current is None:
                print("Index out of bounds.")
                return
            current = current.next

        if current is None:
            print("Index out of bounds.")
            return

        deleted_val = current.data

        if current.next is not None:
            current.next.prev = current.prev

        if current.prev is not None:
            current.prev.next = current.next

        print(f"Deleted {deleted_val} from index {index}.")


# Example Usage / Driver Code
if __name__ == "__main__":
    dll = DoublyLinkedList()

    # Insertions
    dll.insert_at_beginning(20)
    dll.insert_at_beginning(10)
    dll.insert_at_end(40)
    dll.insert_at_index(30, 2)  # Inserts 30 at index 2

    # Display Forward & Backward
    print("\nForward traversal:")
    dll.display_forward()

    print("Backward traversal:")
    dll.display_backward()

    # Deletions
    print("\nDeletions:")
    dll.delete_from_beginning()  # Deletes 10
    dll.display_forward()

    dll.delete_from_end()        # Deletes 40
    dll.display_forward()

    dll.delete_at_index(1)       # Deletes element at index 1 (which is 30)
    dll.display_forward()