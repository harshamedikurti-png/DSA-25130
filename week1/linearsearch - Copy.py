def linearsearch(arr , key ):
    i=0
    for i in range(len(arr)):

        if arr[i] == key :
            return i 
    return -1


result = linearsearch([1,2,3,4,5,6] , 3)

if result != -1 :
    print(f"the index of the target is:{result}")
else:
    print("target not found")

