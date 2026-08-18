def insertionSort(arr):
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j = j - 1

        arr[j + 1] = key

    return arr


# INPUT FROM USER
arr = []

n = int(input("Enter size of the list: "))

print("Enter the elements:")

for i in range(n):
    arr.append(int(input()))

print("Sorted array:")

print(insertionSort(arr))