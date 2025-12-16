from itertools import combinations

def largestPermutation(k, arr):
    # Write your code here
    n = len(arr)
    pos = {v: i for i, v in enumerate(arr)}
    for i in range(n):
        if k == 0:
            break
        if arr[i] != n - i:
            j = pos[n - i]
            arr[i], arr[j] = arr[j], arr[i]
            pos[arr[i]], pos[arr[j]] = i, j
            k -= 1
    return arr


s = [4, 2, 3, 5, 1]
#s = [5, 2, 3, 4, 1]
k = 2
#s = [1,2,3,4,5,6,7,8,9,10]
#s = [7]
#for i in s:
print(largestPermutation(k,s))