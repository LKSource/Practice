from itertools import combinations

def decentNumber(n):
    # Write your code here
    #print(n)
    result = []
    if n % 3 == 0:
        result = ['5']*n
    elif n < 3 or n // 5 == 0:
        result = ['-1']
    else:
        i = n
        t = 0
        f = 0
        while 1:
            #print(i)
            if (i-5) % 3 == 0:
                t = (i-5) // 3
                f +=1
                break
            i -= 5
            if i < 5: return '-1'
            f += 1
        #print(t,f)
        result = ['5']*t*3
        result += ['3']*f*5
    return ''.join(result)

s = [1,3,5,11,4,6,15,13]
#s = [1,2,3,4,5,6,7,8,9,10]
#s = [7]
for i in s:
    print(decentNumber(i))