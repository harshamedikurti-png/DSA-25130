
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:

    # Get height of node
    def height(self, root):
        if root is None:
            return 0
        return root.height

    # Get balance factor
    def get_balance(self, root):
        if root is None:
            return 0
        return self.height(root.left) - self.height(root.right)

    # Right rotation (LL case)
    def right_rotate(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        y.height = 1 + max(
            self.height(y.left),
            self.height(y.right)
        )

        x.height = 1 + max(
            self.height(x.left),
            self.height(x.right)
        )

        return x

    # Left rotation (RR case)
    def left_rotate(self, x):
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        x.height = 1 + max(
            self.height(x.left),
            self.height(x.right)
        )

        y.height = 1 + max(
            self.height(y.left),
            self.height(y.right)
        )

        return y

    # Insertion
    def insert(self, root, key):

        if root is None:
            return Node(key)

        if key < root.key:
            root.left = self.insert(root.left, key)

        elif key > root.key:
            root.right = self.insert(root.right, key)

        else:
            return root

        # Update height
        root.height = 1 + max(
            self.height(root.left),
            self.height(root.right)
        )

        balance = self.get_balance(root)

        # LL Case
        if balance > 1 and key < root.left.key:
            return self.right_rotate(root)

        # RR Case
        if balance < -1 and key > root.right.key:
            return self.left_rotate(root)

        # LR Case
        if balance > 1 and key > root.left.key:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # RL Case
        if balance < -1 and key < root.right.key:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    # Find minimum value node
    def min_value_node(self, root):
        current = root

        while current.left is not None:
            current = current.left

        return current

    # Deletion
    def delete(self, root, key):

        if root is None:
            return root

        if key < root.key:
            root.left = self.delete(root.left, key)

        elif key > root.key:
            root.right = self.delete(root.right, key)

        else:
            # Node with no child or one child
            if root.left is None:
                return root.right

            elif root.right is None:
                return root.left

            # Node with two children
            temp = self.min_value_node(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)

        # Update height
        root.height = 1 + max(
            self.height(root.left),
            self.height(root.right)
        )

        balance = self.get_balance(root)

        # LL Case
        if balance > 1 and self.get_balance(root.left) >= 0:
            return self.right_rotate(root)

        # LR Case
        if balance > 1 and self.get_balance(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # RR Case
        if balance < -1 and self.get_balance(root.right) <= 0:
            return self.left_rotate(root)

        # RL Case
        if balance < -1 and self.get_balance(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    # Searching
    def search(self, root, key):

        if root is None or root.key == key:
            return root

        if key < root.key:
            return self.search(root.left, key)

        return self.search(root.right, key)

    # Inorder traversal
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.key, end=" ")
            self.inorder(root.right)

    # Preorder traversal
    def preorder(self, root):
        if root:
            print(root.key, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    # Postorder traversal
    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.key, end=" ")

    # Display tree with height and balance factor
    def display(self, root):
        if root:
            print(
                "Node:", root.key,
                "Height:", root.height,
                "Balance Factor:", self.get_balance(root)
            )
            self.display(root.left)
            self.display(root.right)


# Main program
avl = AVLTree()
root = None

while True:

    print("\n--- AVL TREE OPERATIONS ---")
    print("1. Insert")
    print("2. Delete")
    print("3. Search")
    print("4. Inorder Traversal")
    print("5. Preorder Traversal")
    print("6. Postorder Traversal")
    print("7. Display Height and Balance Factor")
    print("8. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        key = int(input("Enter value to insert: "))
        root = avl.insert(root, key)
        print("Node inserted successfully")

    elif choice == 2:
        key = int(input("Enter value to delete: "))
        if avl.search(root, key):
            root = avl.delete(root, key)
            print("Node deleted successfully")
        else:
            print("Node not found")

    elif choice == 3:
        key = int(input("Enter value to search: "))
        if avl.search(root, key):
            print("Element found")
        else:
            print("Element not found")

    elif choice == 4:
        print("Inorder:", end=" ")
        avl.inorder(root)
        print()

    elif choice == 5:
        print("Preorder:", end=" ")
        avl.preorder(root)
        print()

    elif choice == 6:
        print("Postorder:", end=" ")
        avl.postorder(root)
        print()

    elif choice == 7:
        print("\nNode details:")
        avl.display(root)

    elif choice == 8:
        print("Exiting...")
        break

    else:
        print("Invalid choice")
