def palindromeIndex(s):
    # Write your code here
    if s == s[::-1]:
        return -1
    n = len(s)
    for i in range(n//2):
        if s[i] != s[n-i-1]:
            new_string = s[:i] + s[i + 1:]
            if new_string == new_string[::-1]:
                return i
            else:
                return n - i - 1

st = ['aaab','baa','aaa']
for s in st:
    print(palindromeIndex(s))

#for s in arr:
#    print(alternatingCharacters(s))  
