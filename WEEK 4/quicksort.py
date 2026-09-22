def quick_sort(arr):
    # Base case: lists with 0 or 1 element are already sorted
    if len(arr) <= 1:
        return arr

    # Choose a pivot (middle element in this case)
    pivot = arr[len(arr) // 2]

    # Partition the array into three sub-lists
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    # Recursively sort left and right, then combine
    return quick_sort(left) + middle + quick_sort(right)