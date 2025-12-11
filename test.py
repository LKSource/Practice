def missingNumbers(arr, brr):
    r = []
    for i in brr:
        if i not in arr:
            r.append(i)
        else:
            arr.remove(i)
    r = list(set(r))
    r.sort()
    return r

k = 4
arr = [203, 204, 205, 206, 207, 208, 203, 204, 205, 206]
brr = [203, 204, 204, 205, 206, 207, 205, 208, 203, 206, 205, 206, 204]
print(missingNumbers(arr, brr))