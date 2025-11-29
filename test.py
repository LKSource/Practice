def quickSort(arr):
    # Write your code here
    left = []
    right = []
    equal = []

    for i in range(0,len(arr)):
        if arr[i] < arr[0]:
            left.append(arr[i])
        elif arr[i] > arr[0]:
            right.append(arr[i])
        else:
            equal.append(arr[i])
    #print(left, equal, right)
    return left + equal + right

arr =[4, 5, 3, 7, 2]
print(quickSort(arr))