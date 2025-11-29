def funnyString(s):
    # Write your code here
    r = s[::-1]
    result = True
    for i in range(1, len(s)):
        if abs(ord(s[i]) - ord(s[i-1])) != abs(ord(r[i]) - ord(r[i-1])):
            result = False
            break

    return 'Funny' if result else 'Not Funny'


d = ['acxz','bcxz']
#d = ['7891011']
for num in d:
    print(funnyString(num))  
