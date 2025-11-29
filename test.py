import string
from itertools import groupby

def weightedUniformStrings1(s, queries):
    # Write your code here
    ref = string.ascii_lowercase
    result = []
    s1 = set(list(s))
    d = {}
    r = ["No"] * len(queries)

#    for c in s1:
#        d.update({c:s.count(c)})

    d = {char: len(list(group)) for char, group in groupby(s)}
    #print(d)
    
    for key, value in d.items():
        weight = ref.index(key) + 1
        for i in range(1, value + 1):
            result.append(weight * i)

    ref_map = {char: ref.index(char) + 1 for char in set(s)}
    result = []

    if s:
        result.append(ref_map[s[0]])
        for i, char in enumerate(s[1:], start=1):
            current_value = ref_map[char]
            if char == s[i-1]:
                result.append(result[-1] + current_value)
            else:
                result.append(current_value)

    comm = list(set(queries).intersection(result))
    indx = []
    for t in comm:
        indx = indx + [index for index, value in enumerate(queries) if value == t]
    
    for t in indx:
        r[t] = "Yes"
    print(ref_map, queries, result, indx, r)
    return (r)
#    print(s1, d, result)
    #return (['Yes' if q in result else 'No' for q in queries])
    #print(result)

def weightedUniformStrings(s, queries):
    # Write your code here
    count = 1
    ref = string.ascii_lowercase
    result = []
    r = ["No"] * len(queries)

    result.append(ref.index(s[0]) + 1)

    for i in range(1,len(s)):
        if s[i] == s[i-1]:
            result.append(result[-1] + ref.index(s[i]) + 1)
        else:
            result.append(ref.index(s[i]) + 1)

    #print(result,queries,list(set(queries).intersection(result)))
    comm = list(set(queries).intersection(result))
    indx = []
    for t in comm:
        indx = indx + [index for index, value in enumerate(queries) if value == t]
    
    for t in indx:
        r[t] = "Yes"

#    for c in range(0,len(queries)):
#        if queries[c] in result:
#            r[c] = "Yes"
        #weight = ref.index(s[i]) + 1
        #result.append(weight * count)
    return (r)
    #return (['Yes' if q in result else 'No' for q in queries])
    #print(result)

def weightedUniformStrings2(s, queries):
    # Write your code here
    pw = set()
    cw = 0

    for i in range(len(s)):
        char = s[i]
        w = ord(char) - ord('a') + 1
        if i == 0 or char != s[i - 1]:
            cw = w  
        else:
            cw += w
        pw.add(cw)
    
    r = ['Yes' if q in pw else 'No' for q in queries]

#    for c in range(0,len(queries)):
#        if queries[c] in result:
#            r[c] = "Yes"
        #weight = ref.index(s[i]) + 1
        #result.append(weight * count)
    return (r)
    #return (['Yes' if q in result else 'No' for q in queries])
    #print(result)

print(weightedUniformStrings2('abbcccddddab', [1, 7, 5, 4, 15, 4, 15,1]))  