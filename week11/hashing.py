
class Hashing:

    def __init__(self, size):
        self.size = size
        self.chaining = [[] for i in range(size)]
        self.linear = [None] * size
        self.quadratic = [None] * size
        self.deleted = "DELETED"

    # Hash function
    def hash_function(self, key):
        return key % self.size

    # ---------------- SEPARATE CHAINING ----------------

    def chaining_insert(self, key):
        index = self.hash_function(key)

        if key not in self.chaining[index]:
            self.chaining[index].append(key)
            print("Inserted successfully")
        else:
            print("Duplicate element")

    def chaining_search(self, key):
        index = self.hash_function(key)

        if key in self.chaining[index]:
            print("Element found")
        else:
            print("Element not found")

    def chaining_delete(self, key):
        index = self.hash_function(key)

        if key in self.chaining[index]:
            self.chaining[index].remove(key)
            print("Element deleted")
        else:
            print("Element not found")

    def chaining_display(self):
        print("Separate Chaining:")
        for i in range(self.size):
            print(i, ":", self.chaining[i])

    # ---------------- LINEAR PROBING ----------------

    def linear_insert(self, key):
        index = self.hash_function(key)

        for i in range(self.size):
            pos = (index + i) % self.size

            if self.linear[pos] == key:
                print("Duplicate element")
                return

            if self.linear[pos] is None or self.linear[pos] == self.deleted:
                self.linear[pos] = key
                print("Inserted successfully")
                return

        print("Hash table is full")

    def linear_search(self, key):
        index = self.hash_function(key)

        for i in range(self.size):
            pos = (index + i) % self.size

            if self.linear[pos] is None:
                print("Element not found")
                return

            if self.linear[pos] == key:
                print("Element found at index", pos)
                return

        print("Element not found")

    def linear_delete(self, key):
        index = self.hash_function(key)

        for i in range(self.size):
            pos = (index + i) % self.size

            if self.linear[pos] is None:
                print("Element not found")
                return

            if self.linear[pos] == key:
                self.linear[pos] = self.deleted
                print("Element deleted")
                return

        print("Element not found")

    def linear_display(self):
        print("Linear Probing:")
        for i in range(self.size):
            print(i, ":", self.linear[i])

    # ---------------- QUADRATIC PROBING ----------------

    def quadratic_insert(self, key):
        index = self.hash_function(key)
        first_deleted = None

        for i in range(self.size):
            pos = (index + i * i) % self.size

            if self.quadratic[pos] == key:
                print("Duplicate element")
                return

            if self.quadratic[pos] == self.deleted:
                if first_deleted is None:
                    first_deleted = pos

            elif self.quadratic[pos] is None:
                if first_deleted is not None:
                    pos = first_deleted

                self.quadratic[pos] = key
                print("Inserted successfully")
                return

        if first_deleted is not None:
            self.quadratic[first_deleted] = key
            print("Inserted successfully")
        else:
            print("No available position")

    def quadratic_search(self, key):
        index = self.hash_function(key)

        for i in range(self.size):
            pos = (index + i * i) % self.size

            if self.quadratic[pos] is None:
                print("Element not found")
                return

            if self.quadratic[pos] == key:
                print("Element found at index", pos)
                return

        print("Element not found")

    def quadratic_delete(self, key):
        index = self.hash_function(key)

        for i in range(self.size):
            pos = (index + i * i) % self.size

            if self.quadratic[pos] is None:
                print("Element not found")
                return

            if self.quadratic[pos] == key:
                self.quadratic[pos] = self.deleted
                print("Element deleted")
                return

        print("Element not found")

    def quadratic_display(self):
        print("Quadratic Probing:")
        for i in range(self.size):
            print(i, ":", self.quadratic[i])


# ---------------- MAIN PROGRAM ----------------

size = int(input("Enter hash table size: "))
h = Hashing(size)

while True:

    print("\n===== HASHING OPERATIONS =====")
    print("1. Separate Chaining")
    print("2. Linear Probing")
    print("3. Quadratic Probing")
    print("4. Exit")

    method = int(input("Choose hashing technique: "))

    if method == 4:
        print("Exiting...")
        break

    if method not in [1, 2, 3]:
        print("Invalid choice")
        continue

    print("\n1. Insert")
    print("2. Search")
    print("3. Delete")
    print("4. Display")

    choice = int(input("Enter operation: "))

    if choice == 4:
        if method == 1:
            h.chaining_display()
        elif method == 2:
            h.linear_display()
        else:
            h.quadratic_display()

    elif choice in [1, 2, 3]:

        key = int(input("Enter element: "))

        if method == 1:
            if choice == 1:
                h.chaining_insert(key)
            elif choice == 2:
                h.chaining_search(key)
            else:
                h.chaining_delete(key)

        elif method == 2:
            if choice == 1:
                h.linear_insert(key)
            elif choice == 2:
                h.linear_search(key)
            else:
                h.linear_delete(key)

        elif method == 3:
            if choice == 1:
                h.quadratic_insert(key)
            elif choice == 2:
                h.quadratic_search(key)
            else:
                h.quadratic_delete(key)

    else:
        print("Invalid operation")
