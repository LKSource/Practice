import string
def alternatingCharacters(s):
    # Write your code here
    count = 0
    if s.count('A') == len(s) or s.count('B') == len(s):
        count = len(s) - 1
    else:
        for i in range(1,len(s)):
            if s[i] == s[i-1]:
                count += 1 
    return count
'''    elif 'AB' in s or 'BA' in s:
        count = len(s.replace('AB',''))
        if count > len(s.replace('BA','')):
            count = len(s.replace('BA',''))
'''


arr = ['AAAA','BBBBB','ABABABAB','BABABA','AAABBB','AAABBBAABB','AABBAABB','ABABABAA','ABBABBAA']
#arr = ['ABBABBAA']

for s in arr:
    print(alternatingCharacters(s))  
