def almostSorted(arr):
    n = len(arr)
    sorted_arr = sorted(arr)
    left = None
    right = None
    for i in range(n):
        if arr[i] != sorted_arr[i]:
            if left is None:
                left = i
            right = i
    if left is None:
        print("yes")
        return
    arr[left], arr[right] = arr[right], arr[left]
    if arr == sorted_arr:
        print(f"yes\nswap {left + 1} {right + 1}")
        return
    # Swap back
    arr[left], arr[right] = arr[right], arr[left]
    arr[left:right+1] = arr[left:right+1][::-1]
    if arr == sorted_arr:
        print(f"yes\nreverse {left + 1} {right + 1}")
        return
    print("no")


a = [[4, 2], [3, 1, 2], [1, 5, 3, 4, 2, 6], [1, 2, 3, 4, 5],
     [1, 3, 2, 4, 5, 6], [1, 5, 4, 3, 2, 6]]
for i in a:
    almostSorted(i)
