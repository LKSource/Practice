import operator
import itertools

def flippingBits(n):
    # Write your code here
    rev = ""
    binary_string_32bit = format(n, '032b')
    for i in binary_string_32bit:
        if i == '0': rev += '1' 
        else: rev += '0'
    return int(rev,2)

print(flippingBits(1))
