def countingSort(arr):
    # Write your code here
    a = [0] * (max(arr) + 1)
    for num in arr:
        a[num] += 1
    r = []
    for index, count in enumerate(a):
        print(f"Index: {index}, Count: {count}")
        for _ in range(count):
            r.append(index)
    return r

d = [1,1,3,2,1]
#d = ['7891011']

print(countingSort(d))  
