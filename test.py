import itertools

def marcsCakewalk(calorie):
    # Write your code here
    calorie.sort(reverse=True)
    r = 0
    for i in range(len(calorie)):
        r += 2**i * calorie[i]
    return r

g = [[1,3,2],[7, 4, 9, 6]]
for i in g:
    print(marcsCakewalk(i))