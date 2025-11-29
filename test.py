def separateNumbers1(s):
    # Write your code here
    r = "NO"

    for i in range(1, len(s)//2+1):
        st = s[0:i]
        num = int(st)
        for j in range(1, len(s)//i):
            num += 1
            st += str(num)
            if st == s:
                r = "YES " + s[0:i]
                break
    #print(r)
    return r

def separateNumbers(s):
    # Write your code here
    t = True
    r = "NO"
    count = 1

    for i in range(1, len(s)//2):
        for j in range(i+1, len(s)//2 +1):
            first = s[0:i]
            second = s[i:j]
            #print(first,second)
            if int(second) - int(first) == 1:
                num = int(second)
                k = j
                valid = True
                #print(first,second)
                while k < len(s):
                    next_num_str = str(num + 1)
                    next_len = len(next_num_str)
                    #print(next_num_str,s[k:k+next_len])
                    if s[k:k+next_len] == next_num_str:
                        num += 1
                        k += next_len
                    else:
                        valid = False
                        break
                if valid and k == len(s):
                    r = "YES " + first
                    t = False
                    break
    return r

d = ['1234','11121314','99100','99910001001','7891011','9899100','999100010001']
d = ['1234','91011','99100','101103','010203','13','1']
d = ['99910001001','7891011','9899100','999100010001']
#d = ['7891011']
for num in d:
    print(separateNumbers1(num))  
