from itertools import combinations

def toys(w):
    # Write your code here
    #print(n)
    w.sort()
    p = 0
    count = 0
    while p < len(w):
        r = w[p]+4
        t = []
        for j in range(p,len(w)):
            if w[j] <= r:
                t.append(w[j])
        count += 1
        p += len(t) 
    return count

s = [1, 2, 3, 21, 7, 12, 14, 21]
#s = [1,2,3,4,5,6,7,8,9,10]
#s = [7]
#for i in s:
print(toys(s))