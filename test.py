def theLoveLetterMystery(s):
    # Write your code here
    count = 0
    n = len(s)
    for i in range(n//2):
        if s[i] != s[n-i-1]:
            count += abs(ord(s[i]) - ord(s[n-i-1]))
    return count

st = ['abc','abcba','abcd','cba']
for s in st:
    print(theLoveLetterMystery(s))

#for s in arr:
#    print(alternatingCharacters(s))  
