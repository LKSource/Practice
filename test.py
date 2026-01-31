def countSort(arr):
    # Write your code here
    n = len(arr)
    half = n // 2
    max_key = 0
    for i in range(n):
        key = int(arr[i][0])
        if key > max_key:
            max_key = key
    buckets = [[] for _ in range(max_key + 1)]
    for idx in range(n):
        key = int(arr[idx][0])
        val = '-' if idx < half else arr[idx][1]
        buckets[key].append(val)
    result = ' '.join(val for bucket in buckets for val in bucket)
    return result


data_input = [
    [0, 'ab'], [6, 'cd'], [0, 'ef'], [6, 'gh'], [4, 'ij'],
    [0, 'ab'], [6, 'cd'], [0, 'ef'], [6, 'gh'], [0, 'ij'],
    [4, 'that'], [3, 'be'], [0, 'to'], [1, 'be'], [5, 'question'],
    [1, 'or'], [2, 'not'], [4, 'is'], [2, 'to'], [4, 'the']
]
print(countSort(data_input))
