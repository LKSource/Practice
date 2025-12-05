def anagram(s):
    # Write your code here
    if len(s) % 2 != 0:
        return -1
    mid = len(s) // 2
    s1 = s[:mid]
    s2 = s[mid:]
    count = 0
    for char in set(s1):
        count += max(0, s1.count(char) - s2.count(char))
    return count

st = ['aaabbb','ab','abc','mnop','xyyx','xaxbbbxx']
for s in st:
    print(anagram(s))

#for s in arr:
#    print(alternatingCharacters(s))  
