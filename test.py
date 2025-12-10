
def same_pattern(x, y):
    if len(x) != len(y):
        return False
    map_x = {}
    map_y = {}
    for idx in range(len(x)):
        if map_x.setdefault(x[idx], idx) != map_y.setdefault(y[idx], idx):
            return False
    return True

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
            if sub == substr:
                count += 1
                continue

            if len(set(sub)) != len(set(substr)):
                continue

            check = True    
            if not same_pattern(substr, sub):
                check = False

            if check:
                count += 1
        c.append(count)
        #print(c)

        #print(ss)
    return c 

'''
            result_list1 = [1 if substr[i] != substr[j] else 0 for i in range(len(substr)) for j in range(i + 1, len(substr))]
            result_list2 = [1 if sub[i] != sub[j] else 0 for i in range(len(sub)) for j in range(i + 1, len(sub))]
            if result_list1 == result_list2:
                print("Matched by result list")
                continue

            c1 = [substr.count(x) for x in set(substr)]
            c2 = [sub.count(x) for x in set(sub)]
            if c1.sort() != c2.sort():
                continue
                

def cpmatch(substr, sub):
    if len(substr) != len(sub):
            return False
    mapping = {}
    seen_sub_chars = set()

    for char_s, char_p in zip(substr, sub):
        if char_s in mapping:
            if mapping[char_s] != char_p:
                return False
        else:
            if char_p in seen_sub_chars:
                return False
            mapping[char_s] = char_p
            seen_sub_chars.add(char_p)            
    return True
                
                
            ran = len(substr)
            mid = ran // 2
            check = True
            m = mid - 1 if ran % 2 == 0 else mid

            if ran >= 3:
                for i in range(mid):
                    if substr[i] == substr[ran-1-i]:
                        if sub[i] != sub[ran-1-i]:
                            check = False
                            break
                    else:
                        if sub[i] == sub[ran-1-i]:
                            check = False
                            break

                    if substr[i] == substr[i+1]:
                        if sub[i] != sub[i+1]:
                            check = False
                            break
                    else:
                        if sub[i] == sub[i+1]:
                            check = False
                            break

                    if substr[i+m] == substr[i+m+1]:
                        if sub[i+m] != sub[i+m+1]:
                            check = False
                            break
                    else:
                        if sub[i+m] == sub[i+m+1]:
                            check = False
                            break

                if ran % 2 == 1:
                    if substr[mid-1] == substr[mid+1]:
                        if sub[mid-1] != sub[mid+1]:
                            check = False
                    else:
                        if sub[mid-1] == sub[mid+1]:
                            check = False

            if check == False:
                continue
                
                
            for i in range(0,len(substr)):
                for j in range(i+1, len(substr)):
                    if substr[i] == substr[j]:
                        if sub[i] != sub[j]:
                            check = False
                            break
                    else:
                        if sub[i] == sub[j]:
                            check = False
                            break 
                if check == False:
                    break
'''


n = 8
s = "giggabajgiggabaj"
s = "giggabaj"
queries = [[1,1],[1,2],[1,3],[2,4]]
#queries = [[1,7],[1,6]]
print(similarStrings(len(s), s, queries))
#print(similarStrings1(8, s, queries))
#print(similarStrings_optimized(5, s, queries))
#result_list = [1 if s[i] != s[j] else 0 for i in range(len(s)) for j in range(i + 1, len(s))]
#print(result_list)


