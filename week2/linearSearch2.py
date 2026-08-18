def linear(arr, key):
    for i in range(len(arr)): 
        if arr[i] == key:
            return i 
    return -1

def main():
    n = int(input("get me :\t"))
    if n <= 0:
        print("Try again	")
        return  


    arr = []


    for i in range(n):
        s = int(input(f"get me the element {i+1}:\t")) 
        arr.append(s)

    key = int(input("get me the value to search:\t"))
 
    if linear(arr, key) != -1:
        print(f"The {key} is found in array")
    else:
        print("Not found")


main()
