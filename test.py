def countSort(arr):
    # Write your code here
    result = []
    for i in range(len(arr)//2):
        arr[i][1] = '-'
    maxint = max([int(arr[i][0]) for i in range(len(arr))])
    for i in range(maxint+1):
        temp = []
        for j in range(len(arr)):
            if int(arr[j][0]) == i:
                temp.append(arr[j][1])
        result.extend(temp)
    return result

arr = [[0, 'ab'],
[6, 'cd'],
[0, 'ef'],
[6, 'gh'],
[4, 'ij'],
[0, 'ab'],
[6, 'cd'],
[0, 'ef'],
[6, 'gh'],
[0, 'ij'],
[4, 'that'],
[3, 'be'],
[0, 'to'],
[1, 'be'],
[5, 'question'],
[1, 'or'],
[2, 'not'],
[4, 'is'],
[2, 'to'],
[4, 'the']]
print(countSort(arr))
