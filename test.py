def check(s):
    s1 = list(set(s))
    s1.sort()
    print(s1)
    r = []
    s3 = s
    for i in s1:
        s3 = s.replace(i,"")
        print(s3)
        s4 = ''.join(set(s3))
        #print(s3,s.count(s4),s.count(s4[::-1]),len(s3)//2)
        #print(s.count(s4[::-1]) == len(s3)//2 or s.count(s4) == len(s3)//2, len(s3))
        if (s.count(s4[::-1]) == len(s3)//2 or s.count(s4) == len(s3)//2):
            r.append(len(s3))
    print(r)
    return max(r) if r else 0    

def alternate(s):
    sc = set()
    uc = []

    for char in s:
        if char not in sc:
            sc.add(char)
            uc.append(char)

    s1 = "".join(uc)
    #print((s1))
    r = []
    max_length = 0
    for i in range(0,len(s1)):
        for j in range(i+1,len(s1)):
            #print(s1[i],s1[j])
#            s2 = s.replace(s1[i],"")
            s3 = s
            for c in s1:
                if c != s1[i] and c != s1[j]:
#                s2 = s2.replace(c,"")
                   s3 = s3.replace(c,"")
            #print(s3)
            #s4 = ''.join(set(s3))
            l = len(s3)
            valid = True
            for k in range(1, l):
                if s3[k] == s3[k-1]:
                    valid = False
                    break
                    
            if l > max_length and valid:
                max_length = l
            #print(s4)
            #print(s3,s.count(s4),s.count(s4[::-1]),len(s3)//2)
            #print(s.count(s4[::-1]) == len(s3)//2 or s.count(s4) == len(s3)//2, len(s3))
            #if (s3[0:len(s3)//2 * 2].count(s4[::-1]) == len(s3)//2 or s3[0:len(s3)//2 * 2].count(s4) == len(s3)//2):
                #r.append(len(s3))
                #print(len(s3),s3)
        #print(s)
    return max_length
        # Write your code here

#s = 'beabeefeab'
s = 'asdcbsdcagfsdbgdfanfghbsfdab'
print(alternate(s))


s = 'beabeefeab'
x = []
for c in s:
    if c not in x:
        x.append(c)



#print(x)