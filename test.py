def twoStrings(s1, s2):
    # Write your code here
    for char in set(s1):
        if char in s2:
            return "YES"
    return "NO"

print(twoStrings('hello','world'))
#print(makingAnagrams('cde','abc'))
#for s in arr:
#    print(alternatingCharacters(s))  
