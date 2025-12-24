
from collections import defaultdict

def commonChild(s1, s2):
    n = len(s1)
    m = len(s2)
    # Create a 2D DP table with (n+1) rows and (m+1) cols
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[n][m]

def commonChild1(s1, s2):
    # Write your code here
    s1 = list(s1)
    s2 = list(s2)
    r = []
    print(len(s1))
    c = 0
    for k in range(len(s1)):
        count = 0
        m = 0
        t = []
        for i in range(k, len(s1)):
            #print(s1[i])
            for j in range(m,len(s2)):
                if s1[i] == s2[j]:
                    m = j + 1 
                    count += 1
                    t.append(s1[i])
                    #print(s2[j])
                    break
        r.append(count)
        print(count, t)
        c += 1
        #print("\n")
        if len(s1) - k - 1 <= max(r): break
    print(c)
    return max(r)

s1 = 'WEWOUCUIDGCGTRMEZEPXZFEJWISRSBBSYXAYDFEJJDLEBVHHKS'
s2 = 'FDAGCXGKCTKWNECHMRXZWMLRYUCOCZHJRRJBOAJOQJZZVUYXIC'
print(commonChild(s1, s2))