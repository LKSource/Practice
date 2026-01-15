def issorted(arr):
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))


def almostSorted(arr):
    # Write your code here
    print("Array:", arr)
    if issorted(arr):
        print("yes")
        return

    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            arr[i], arr[j] = arr[j], arr[i]
            if issorted(arr):
                print(f"yes\nswap {i + 1} {j + 1}")
                return
            arr[i], arr[j] = arr[j], arr[i]
    
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            arr[i:j + 1] = reversed(arr[i:j + 1])
            if issorted(arr):
                print(f"yes\nreverse {i + 1} {j + 1}")
                return
            arr[i:j + 1] = reversed(arr[i:j + 1])        

    print("no")

a = [[4, 2], [3, 1, 2], [1, 5, 3, 4, 2, 6], [1, 2, 3, 4, 5],
     [1, 3, 2, 4, 5, 6], [1, 5, 4, 3, 2, 6]]
for i in a:
    almostSorted(i)
b = [1, 2, 3, 5, 4, 6]
b[1:4] = reversed(b[1:4])
print(b)
