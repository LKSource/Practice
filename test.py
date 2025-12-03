def findMedian(arr):
    # Write your code here
    arr.sort()
    return arr[len(arr)//2]

arr = [0,1,2,4,6,5,3]

print(findMedian(arr))

#for s in arr:
#    print(alternatingCharacters(s))  
