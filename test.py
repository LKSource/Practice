from itertools import combinations

def jimOrders(orders):
    # Write your code here
    result = []
    d = {}
    for i in range(len(orders)):
        t = sum(orders[i])
        r = [i+1]
        if t in d:
            d[t] += r 
            d[t].sort()
        else:
            d[t] = r
    for i in sorted(d):
        result += d[i]
    return result

s = [[8,1],[4,2],[5,6],[3,1],[4,3]]
#s = [1, 2, 3, 4]
#k = 50
#k = 7
#s = [1,2,3,4,5,6,7,8,9,10]
#s = [7]
#for i in s:
print(jimOrders(s))