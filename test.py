def gameOfThrones(s):
    # Write your code here
    count = 0
    for char in set(s):
        count += max(0, s.count(char) % 2)
    if count > 1:
        return "NO"
    elif len(s) % 2 == 0 and count == 0:
        return "YES"
    elif len(s) % 2 == 1 and count == 1:
        return "YES"
    else:     
        return "NO"

print(gameOfThrones('cdcdcdcdeeeef'))
#print(makingAnagrams('cde','abc'))
#for s in arr:
#    print(alternatingCharacters(s))  
