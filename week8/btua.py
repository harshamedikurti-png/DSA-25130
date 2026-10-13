class BinaryTreeArray:
    def __init__(self, size):
        self.tree = [None] * size
        self.size = size

    def insert(self, value):
        for i in range(self.size):
            if self.tree[i] is None:
                self.tree[i] = value
                print(value, "inserted")
                return
        print("Tree is full")

    def search(self, value):
        for i in range(self.size):
            if self.tree[i] == value:
                print("Value found at index", i)
                return
        print("Value not found")

    def inorder(self, i=0):
        if i < self.size and self.tree[i] is not None:
            self.inorder(2 * i + 1)
            print(self.tree[i], end=" ")
            self.inorder(2 * i + 2)

    def preorder(self, i=0):
        if i < self.size and self.tree[i] is not None:
            print(self.tree[i], end=" ")
            self.preorder(2 * i + 1)
            self.preorder(2 * i + 2)

    def postorder(self, i=0):
        if i < self.size and self.tree[i] is not None:
            self.postorder(2 * i + 1)
            self.postorder(2 * i + 2)
            print(self.tree[i], end=" ")

    def delete(self, value):
        for i in range(self.size):
            if self.tree[i] == value:
                self.tree[i] = None
                print(value, "deleted")
                return
        print("Value not found")

    def display(self):
        print(self.tree)


bt = BinaryTreeArray(10)

while True:
    print("\n1.Insert  2.Search  3.Inorder")
    print("4.Preorder  5.Postorder  6.Delete")
    print("7.Display  8.Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        bt.insert(int(input("Enter value: ")))
    elif choice == 2:
        bt.search(int(input("Enter value: ")))
    elif choice == 3:
        bt.inorder()
        print()
    elif choice == 4:
        bt.preorder()
        print()
    elif choice == 5:
        bt.postorder()
        print()
    elif choice == 6:
        bt.delete(int(input("Enter value: ")))
    elif choice == 7:
        bt.display()
    elif choice == 8:
        break
    else:
        print("Invalid choice")