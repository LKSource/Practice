import operator
import itertools

def sumXor(n):
    # Write your code here
    if n == 0:
        return 1
    zero_bits = n.bit_length() - n.bit_count()
    return 1 << zero_bits
#    lst1 = [n+i for i in range(n+1)]
#    lst2 = [operator.xor(n, i) for i in range(n+1)]
#    for i, j in zip(lst1,lst2):
#        if i == j:
#            count += 1
#    print(lst1, lst2, count)
#    for i in range(n + 1)z
#        if n + i == operator.xor(n , i):
#            count += 1
#    return count

s = [[8,1],[4,2],[5,6],[3,1],[4,3]]
#s = [1, 2, 3, 4]
#k = 50
#k = 7
#s = [1,2,3,4,5,6,7,8,9,10]
#s = [7]
#for i in s:
A = [2, 1, 3]
B = [0,0,1,2,1]
k = 10
l = 10
r = 15
print(sumXor(1000000000000000))
n = 1000000000000000
bits = n.bit_length()  # number of bits
ones = n.bit_count()   # number of 1s (Python 3.10+)
zeros = bits - ones
answer = 2 ** zeros
print(answer)