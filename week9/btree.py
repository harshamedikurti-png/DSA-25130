
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:

    # Insertion
    def insert(self, root, data):
        if root is None:
            return Node(data)

        if data < root.data:
            root.left = self.insert(root.left, data)
        elif data > root.data:
            root.right = self.insert(root.right, data)

        return root

    # Searching
    def search(self, root, key):
        if root is None or root.data == key:
            return root

        if key < root.data:
            return self.search(root.left, key)

        return self.search(root.right, key)

    # Inorder Traversal (Left, Root, Right)
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)

    # Preorder Traversal (Root, Left, Right)
    def preorder(self, root):
        if root:
            print(root.data, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    # Postorder Traversal (Left, Right, Root)
    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data, end=" ")

    # Find minimum value
    def find_min(self, root):
        while root.left:
            root = root.left
        return root

    # Deletion
    def delete(self, root, key):
        if root is None:
            return root

        if key < root.data:
            root.left = self.delete(root.left, key)

        elif key > root.data:
            root.right = self.delete(root.right, key)

        else:
            # Case 1: No child
            if root.left is None and root.right is None:
                return None

            # Case 2: One child
            elif root.left is None:
                return root.right

            elif root.right is None:
                return root.left

            # Case 3: Two children
            temp = self.find_min(root.right)
            root.data = temp.data
            root.right = self.delete(root.right, temp.data)

        return root


# Main program
bst = BST()
root = None

while True:
    print("\n\n1. Insert")
    print("2. Search")
    print("3. Delete")
    print("4. Inorder Traversal")
    print("5. Preorder Traversal")
    print("6. Postorder Traversal")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        data = int(input("Enter value: "))
        root = bst.insert(root, data)
        print("Node inserted successfully")

    elif choice == 2:
        key = int(input("Enter value to search: "))
        result = bst.search(root, key)

        if result:
            print("Element found")
        else:
            print("Element not found")

    elif choice == 3:
        key = int(input("Enter value to delete: "))
        root = bst.delete(root, key)
        print("Deletion operation completed")

    elif choice == 4:
        print("Inorder:", end=" ")
        bst.inorder(root)

    elif choice == 5:
        print("Preorder:", end=" ")
        bst.preorder(root)

    elif choice == 6:
        print("Postorder:", end=" ")
        bst.postorder(root)

    elif choice == 7:
        print("Exiting...")
        break

    else:
        print("Invalid choice")
