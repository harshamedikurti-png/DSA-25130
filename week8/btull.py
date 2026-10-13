class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTreeLinked:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)

        if self.root is None:
            self.root = new_node
            return

        queue = [self.root]

        while queue:
            current = queue.pop(0)

            if current.left is None:
                current.left = new_node
                return
            queue.append(current.left)

            if current.right is None:
                current.right = new_node
                return
            queue.append(current.right)

    def search(self, root, value):
        if root is None:
            return False
        if root.data == value:
            return True

        return (self.search(root.left, value) or
                self.search(root.right, value))

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)

    def preorder(self, root):
        if root:
            print(root.data, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data, end=" ")

    def delete(self, value):
        if self.root is None:
            print("Tree is empty")
            return

        queue = [self.root]
        target = None
        deepest = None
        parent = None

        while queue:
            current = queue.pop(0)

            if current.data == value and target is None:
                target = current

            if current.left:
                parent = current
                queue.append(current.left)

            if current.right:
                parent = current
                queue.append(current.right)

            deepest = current

        if target is None:
            print("Value not found")
            return

        if deepest == self.root and target == self.root:
            self.root = None
        elif target == deepest:
            if parent.left == deepest:
                parent.left = None
            else:
                parent.right = None
        else:
            target.data = deepest.data
            if parent.right == deepest:
                parent.right = None
            else:
                parent.left = None

        print(value, "deleted")

    def display(self):
        print("Inorder:", end=" ")
        self.inorder(self.root)
        print()


bt = BinaryTreeLinked()

while True:
    print("\n1.Insert  2.Search  3.Inorder")
    print("4.Preorder  5.Postorder  6.Delete")
    print("7.Display  8.Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        bt.insert(int(input("Enter value: ")))
    elif choice == 2:
        value = int(input("Enter value: "))
        if bt.search(bt.root, value):
            print("Value found")
        else:
            print("Value not found")
    elif choice == 3:
        bt.inorder(bt.root)
        print()
    elif choice == 4:
        bt.preorder(bt.root)
        print()
    elif choice == 5:
        bt.postorder(bt.root)
        print()
    elif choice == 6:
        bt.delete(int(input("Enter value: ")))
    elif choice == 7:
        bt.display()
    elif choice == 8:
        break
    else:
        print("Invalid choice")