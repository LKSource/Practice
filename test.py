def makingAnagrams(s1, s2):
    # Write your code here
    count = 0
    for char in set(s1):
        count += max(0, s1.count(char) - s2.count(char))
    for char in set(s2):
        count += max(0, s2.count(char) - s1.count(char))
    return count

print(makingAnagrams('abc','amnop'))
print(makingAnagrams('cde','abc'))
#for s in arr:
#    print(alternatingCharacters(s))  
