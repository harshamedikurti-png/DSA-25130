def bubbleSort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


# INPUT FROM USER
arr = []

n = int(input("Enter size of the list: "))

print("Enter the elements:")

for i in range(n):
    arr.append(int(input()))

print("Sorted array:")

print(bubbleSort(arr))