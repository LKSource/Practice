import string

def fibonacci(n):
    """Return the nth Fibonacci number."""
    if n <= 0:
        return "Input should be a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n):
            a, b = b, a + b
        return b

def is_palindrome(s):
    """Check if the given string is a palindrome."""
    s = s.lower().replace(" ", "")
    s = ''.join(char for char in s if char.isalnum())
    for i in range(len(s) // 2):
        if s[i] != s[-(i + 1)]:
            return False
    return True

def superReducedString(s):
    # Write your code here
    for char in set(s):
        double_char = char * 2
        while double_char in s:
            s = s.replace(double_char, "")
            s = superReducedString(s)
    if s == "" :
        return 'Empty String'
    else:
        return s

def camelcase(s):
    # Write your code here
    count = sum(1 for char in s if char.isupper())
    return count + 1

def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"

    has_number = any(char in numbers for char in password)
    has_lower = any(char in lower_case for char in password)
    has_upper = any(char in upper_case for char in password)
    has_special = any(char in special_characters for char in password)   
 
    s = 4 - (has_number + has_lower + has_upper + has_special)

    if s + len(password) >= 6:
        return(s)
    else:
        return(6 - len(password))

greekAlphabet = ['Alpha', 'Beta', 'Gamma', 'Delta', 'Theta']

def my_decorator(func):
    def wrapper(*args, **kwargs):
        for key, value in kwargs.items():
            kwargs[key] = value.capitalize()
        result = func(*args, **kwargs)
        return result
    return wrapper

@my_decorator
def isGreekAlphabet(name):
    return "True" if name in greekAlphabet else "False"

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

def hackerrankInString(s):
    # Write your code here
    ref = "hackerrank"
    target = []
    t = []

    i = 0
    for char in ref:
        while i < len(s) and char != s[i]:
            i += 1
        if i < len(s) :
            if char == s[i]:
                #print(i)                
                t.append(i)
                target.append(char)
                i += 1 
    #print(target)                
    return 'YES' if ref == ''.join(target) else 'NO'

def caesarCipher(s, k):
    # Write your code here
    b = string.ascii_lowercase
    r = []
    
    for char in s:
        if char in string.ascii_lowercase:
            index = (string.ascii_lowercase.index(char) + k +1) % 26
            if index == 0:
                index = 26
            r.append(b[index-1])
        elif char in string.ascii_uppercase:
            index = (string.ascii_uppercase.index(char) + k +1) % 26
            if index == 0:
                index = 26
            r.append(b[index-1].upper())
        else:
            r.append(char)
    return(''.join(r))

def marsExploration(s):
    r = "SOS"
    # Write your code here
    if len(s) % 3 != 0:
        return 0
    count = 0
    for i in range(0,len(s)//3):
        s1 = s[i*3:i*3+3]
        count += sum(1 for a, b in zip(s1, r) if a != b)
    return count

def quickSort(arr):
    # Write your code here
    left = []
    right = []
    equal = []

    for i in range(0,len(arr)):
        if arr[i] < arr[0]:
            left.append(arr[i])
        elif arr[i] > arr[0]:
            right.append(arr[i])
        else:
            equal.append(arr[i])
    #print(left, equal, right)
    return left + equal + right

def pangrams(s):
    # Write your code here
    count = 0
    ref = string.ascii_lowercase
    s = s.lower()
    for char in ref:
        if char in s:
            count += 1
    if count == 26:       
        return 'pangram'
    else:
        return 'not pangram'
    
def weightedUniformStrings(s, queries):
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

    return (r)

def separateNumbers(s):
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

def funnyString(s):
    # Write your code here
    r = s[::-1]
    result = True
    for i in range(1, len(s)):
        if abs(ord(s[i]) - ord(s[i-1])) != abs(ord(r[i]) - ord(r[i-1])):
            result = False
            break

    return 'Funny' if result else 'Not Funny'

def countingSort(arr):
    # Write your code here
    a = [0] * (max(arr) + 1)
    for num in arr:
        a[num] += 1
    r = []
    for index, count in enumerate(a):
        for _ in range(count):
            r.append(index)
    return r

def gemstones(arr):
    # Write your code here
    ref = string.ascii_lowercase

    for s in arr:
        ref = ''.join([c for c in ref if c in s])
    #print(ref)
    return len(ref)

def alternatingCharacters(s):
    # Write your code here
    count = 0
    if s.count('A') == len(s) or s.count('B') == len(s):
        count = len(s) - 1
    else:
        for i in range(1,len(s)):
            if s[i] == s[i-1]:
                count += 1 
    return count

def beautifulBinaryString(b):
    # Write your code here
    count = b.count('010')
    return count

def closestNumbers(arr):
    # Write your code here
    arr.sort()
    min_diff = float('inf')
    result = []
    for i in range(len(arr) - 1):
        diff = arr[i + 1] -  arr[i]
        if diff < min_diff:
            min_diff = diff
            result = [arr[i], arr[i + 1]]
        elif diff == min_diff:
            result.append(arr[i])
            result.append(arr[i + 1])
    return result

def findMedian(arr):
    # Write your code here
    arr.sort()
    return arr[len(arr)//2]

def theLoveLetterMystery(s):
    # Write your code here
    count = 0
    n = len(s)
    for i in range(n//2):
        if s[i] != s[n-i-1]:
            count += abs(ord(s[i]) - ord(s[n-i-1]))
    return count

def palindromeIndex(s):
    # Write your code here
    if s == s[::-1]:
        return -1
    n = len(s)
    for i in range(n//2):
        if s[i] != s[n-i-1]:
            new_string = s[:i] + s[i + 1:]
            if new_string == new_string[::-1]:
                return i
            else:
                return n - i - 1
            
def anagram(s):
    # Write your code here
    if len(s) % 2 != 0:
        return -1
    mid = len(s) // 2
    s1 = s[:mid]
    s2 = s[mid:]
    count = 0
    for char in set(s1):
        count += max(0, s1.count(char) - s2.count(char))
    return count

def makingAnagrams(s1, s2):
    # Write your code here
    count = 0
    for char in set(s1):
        count += max(0, s1.count(char) - s2.count(char))
    for char in set(s2):
        count += max(0, s2.count(char) - s1.count(char))
    return count

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

def twoStrings(s1, s2):
    # Write your code here
    for char in set(s1):
        if char in s2:
            return "YES"
    return "NO"

def stringConstruction(s):
    # Write your code here
    return len(set(s))

def knightlOnAChessboard(n):
    # Write your code here
    arr = []
    for i in range(1, n):
        results = []
        for j in range(1, n):
            r = []
            #print(f"({i},{j})", end=" ")
            # Implement BFS or DFS to find the shortest path
            from collections import deque
            visited = [[False]*n for _ in range(n)]
            queue = deque()
            queue.append((0, 0, 0))  # (x, y,
            visited[0][0] = True
            found = False
            while queue:
                x, y, dist = queue.popleft()
                if x == n-1 and y == n-1:
                    r.append(dist)
                    found = True
                    break
                for dx, dy in [(i, j), (i, -j), (-i, j), (-i, -j), (j, i), (j, -i), (-j, i), (-j, -i)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                        visited[nx][ny] = True
                        queue.append((nx, ny, dist + 1))
            if found:
                #print(r[0], end=" ")
                results.append(r[0])
            else:
                #print(-1, end=" ")  
                results.append(-1)
        #print(results)
        arr.append(results)    
        #print()
    return arr

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

def icecreamParlor(m, arr):
    cost_map = {}
    for i, cost in enumerate(arr):
        complement = m - cost
        if complement in cost_map:
            return (cost_map[complement] + 1, i + 1)
        cost_map[cost] = i
    return None

def missingNumbers(arr, brr):
    r = []
    for i in brr:
        if i not in arr:
            r.append(i)
        else:
            arr.remove(i)
    r = list(set(r))
    r.sort()
    return r

def beautifulPairs(A, B):
    
    count = 0
    ref = []

    for i in range(len(A)):
        check = False
        for j in range(len(B)):
            if A[i] == B[j]:
                if j not in ref:
                    check = True
                    ref.append(j)
                    count += 1
            if check:
                break
    if count == len(A):
        count -= 1
    else:
        count += 1
    return count

def balancedSums(arr):
    # Write your code here
    total = sum(arr)
    left_sum = 0
    for num in arr:
        if left_sum == total - left_sum - num:
            return "YES"
        left_sum += num
    return "NO"

import itertools

def minimumAbsoluteDifference(arr):
    # Write your code here
    arr.sort()  
    min_diff = float('inf')
    
    for i in range(1, len(arr)):
        diff = arr[i] - arr[i - 1]  
        if diff < min_diff:
            min_diff = diff
        if min_diff == 0:  
            break
    
    return min_diff

def marcsCakewalk(calorie):
    # Write your code here
    calorie.sort(reverse=True)
    r = 0
    for i in range(len(calorie)):
        r += 2**i * calorie[i]
    return r

def gridChallenge(grid):
    # Write your code here
#    print(grid)
    for i in range(len(grid)):
        g = list(grid[i])
        g.sort()
#        print(g)
        grid[i] = g
        #print(grid[i].split())
    check = True
    tl = list(map(list, zip(*grid)))
    for t in tl:
        t1 = t.copy()
        t1.sort()
        if t != t1:
            check = False
            break
    return "YES" if check else "NO"

def luckBalance(k, contests):
    # Write your code here
#    print(grid)
    im = []
    ni = []
    for i in contests:
        if i[1]: im.append(i[0]) 
        else: ni.append(i[0])
    im.sort(reverse=True)
    result = sum(im[0:k])+sum(ni)-(sum(im)-sum(im[0:k]))
#    print(sum(im[0:k]),sum(ni),result)
#    print(im, ni) 
    return result

from itertools import combinations
def maximumPerimeterTriangle(sticks):
    # Write your code here
    r = float('-inf')
    c = combinations(sticks, 3)
    c = list(c)
    #print(c)
    l = []
    for i in c:
        i = list(i)
        i.sort()
        if i[0]+i[1] == i[2]:
            continue
        if i[0]+i[1] > i[2] and sum(i) > r:
            r = sum(i)
            l = i
#
    return [-1] if not l else l

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

def toys(w):
    # Write your code here
    #print(n)
    w.sort()
    p = 0
    count = 0
    while p < len(w):
        r = w[p]+4
        t = []
        for j in range(p,len(w)):
            if w[j] <= r:
                t.append(w[j])
        count += 1
        p += len(t) 
    return count

def largestPermutation(k, arr):
    # Write your code here
    n = len(arr)
    pos = {v: i for i, v in enumerate(arr)}
    for i in range(n):
        if k == 0:
            break
        if arr[i] != n - i:
            j = pos[n - i]
            arr[i], arr[j] = arr[j], arr[i]
            pos[arr[i]], pos[arr[j]] = i, j
            k -= 1
    return arr

def maximumToys(prices, k):
    # Write your code here
    prices.sort()
#    print(prices)
    c = 0
    count = 0
    for p in prices:
        c += p
        if c > k: break
        count += 1
    return count

def jimOrders(orders):
    # Write your code here
    result = []
    d = {}
    for i in range(len(orders)):
        t = sum(orders[i])
        r = [i+1]
        if t in d:
            d[t] += r 
            d[t].sort()
        else:
            d[t] = r
    for i in sorted(d):
        result += d[i]
    return result

def twoArrays(k, A, B):
    # Write your code here
    A.sort()
    B.sort(reverse=True)
    check = True
    for i in range(len(A)):
        if A[i] + B[i] < k:
            check = False
    return 'YES' if check else 'NO'

def lonelyinteger(a):
    # Write your code here
    result = [r for r in a if a.count(r)==1]
    return result[0]

import operator
import itertools

def maximizingXor(l, r):
    # Write your code here
    lst = []
    for i in range(l,r+1):
        lst += [i]
    plst = list(itertools.permutations(lst, r=2))
    result = 0
    for i in plst:
        t = operator.xor(i[0],i[1])
        if t > result:
            result = t
    return result

def sumXor(n):
    # Write your code here
    if n == 0:
        return 1
    zero_bits = n.bit_length() - n.bit_count()
    return 1 << zero_bits

def flippingBits(n):
    # Write your code here
    rev = ""
    binary_string_32bit = format(n, '032b')
    for i in binary_string_32bit:
        if i == '0': rev += '1' 
        else: rev += '0'
    return int(rev,2)

def gameOfStones(n):
    # Write your code here
    if n % 7 in (0, 1):
        return 'Second'
    else:
        return 'First'