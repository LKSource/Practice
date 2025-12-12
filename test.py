def balancedSums(arr):
    # Write your code here
    total = sum(arr)
    left_sum = 0
    for num in arr:
        if left_sum == total - left_sum - num:
            return "YES"
        left_sum += num
    return "NO"

g = [[1,2,3],[1,1,4,1],[2,0,0,0],[0,0,2,0],[1,2,3,3],[0,0,0,2]]
for i in g:
    print(balancedSums(i))