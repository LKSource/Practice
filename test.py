import string
def beautifulBinaryString(b):
    # Write your code here
    count = b.count('010')
    return count

arr = ['AAAA','BBBBB','ABABABAB','BABABA','AAABBB','AAABBBAABB','AABBAABB','ABABABAA','ABBABBAA']
arr = '0100101010'

print(beautifulBinaryString(arr))

#for s in arr:
#    print(alternatingCharacters(s))  
