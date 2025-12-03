import string
def closestNumbers(arr):
    # Write your code here
    arr.sort()
    min_diff = float('inf')
    result = []
    for i in range(len(arr) - 1):
        diff = arr[i + 1] -  arr[i]
        if diff < min_diff:
            min_diff = diff
            result = [arr[i], arr[i + 1]]
        elif diff == min_diff:
            result.append(arr[i])
            result.append(arr[i + 1])
    return result

arr = [5,4,3,2]

print(closestNumbers(arr))

#for s in arr:
#    print(alternatingCharacters(s))  
