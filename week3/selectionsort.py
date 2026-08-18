def selectionSort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


# INPUT FROM USER
arr = []

n = int(input("Enter size of the list: "))

print("Enter the elements:")

for i in range(n):
    arr.append(int(input()))

print("Sorted array:")

print(selectionSort(arr))