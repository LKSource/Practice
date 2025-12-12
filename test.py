import itertools

def minimumAbsoluteDifference(arr):
    # Write your code here
    arr.sort()  
    min_diff = float('inf')
    
    for i in range(1, len(arr)):
        diff = arr[i] - arr[i - 1]  
        if diff < min_diff:
            min_diff = diff
        if min_diff == 0:  
            break
    
    return min_diff

g = [[3,-7,0],[-59,-36 ,-13, 1, -53, -92, -2, -96, -54, 75]]
for i in g:
    print(minimumAbsoluteDifference(i))