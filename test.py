from itertools import combinations

def maximumToys(prices, k):
    # Write your code here
    prices.sort()
#    print(prices)
    c = 0
    count = 0
    for p in prices:
        c += p
        if c > k: break
        count += 1
    return count

s = [1, 12, 5, 111, 200, 1000, 10]
s = [1, 2, 3, 4]
k = 50
k = 7
#s = [1,2,3,4,5,6,7,8,9,10]
#s = [7]
#for i in s:
print(maximumToys(s,k))