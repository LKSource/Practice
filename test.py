def isValid(s):
    # Write your code here
    r = []
    for i in set(s):
        r.append(s.count(i))
#    print(r,set(r))
    if len(set(r)) == 1 : return "YES"
    else: 
        for i in set(r):
#            print(r.count(i))
            if r.count(i) == 1:
#                print([r.index(i)])
                r[r.index(i)] = r[r.index(i)] - 1
                if 0 in r: r.remove(0)
                break
        return "YES" if len(set(r)) == 1 else "NO"

s = 'aabbcccdd'
print(isValid(s))