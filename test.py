def similarStrings(n, s, queries):
    # Write your code here
    c = []
    for query in queries:
        l = query[0]
        r = query[1]
        substr = s[l-1:r]
        if len(substr) == 1:
            c.append(len(s))
            continue
        #print(substr)
        ss = [s[i:i+r-l+1] for i in range(len(s)) if i+r-l+1 <= len(s)]
#        print(substr)
#        print(ss)
        count = 0
        for sub in ss:
            check = True
            for i in range(0,len(substr)):
                for j in range(i+1, len(substr)):
#                    print(i,j)
#                    print(substr[i], substr[j], sub[i], sub[j])
                    if (substr[i] == substr[j] and sub[i] == sub[j]) or (substr[i] != substr[j] and sub[i] != sub[j]):
                        continue
#                        check = True
                    else:
                        check = False
                        break
            if check:
                count += 1
        c.append(count)
        #print(c)

        #print(ss)
    return c 

n = 8
s = "giggabaj"
queries = [[1,1],[1,2],[1,3],[2,4]]
#queries = [[2,4]]
print(similarStrings(5, s, queries))

