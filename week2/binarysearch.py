def binary(arr, key):
    llimit, rlimit = 0, len(arr) - 1

    while llimit <= rlimit:
        mid = (llimit + rlimit) // 2

        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            llimit = mid + 1
        else:
            rlimit = mid - 1

    return -1


def main():
    n = int(input("Enter the size of the list: "))

    if n <= 0:
        print("Invalid size")
        return

    arr = []

    for i in range(n):
        arr.append(int(input(f"Enter element {i + 1}: ")))

    key = int(input("Enter the element to search: "))

    if arr != sorted(arr):
        print("Sorting array")
        arr.sort()

    print(f"Sorted array: {arr}")

    index = binary(arr, key)

    if index != -1:
        print(f"{key} found at index {index}")
    else:
        print("Element not found")


main()