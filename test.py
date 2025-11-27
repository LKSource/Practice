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

print("SOSSPSSQSSOR")
print(marsExploration("SOSSPSSQSSOR"))