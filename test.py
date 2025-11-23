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


'''
    for char in s:
        if char in ref:
            if char not in target:
                target.append(char)
    print(target)
'''
#print(hackerrankInString("hereiamstackerrank"))
#print(hackerrankInString("hackerworld"))

test = []
test.append('knarrekcah')
test.append('hackerrank')
test.append('hackeronek')
test.append('abcdefghijklmnopqrstuvwxyz')
test.append('rhackerank')
test.append('ahankercka')
test.append('hacakaeararanaka')
test.append('hhhhaaaaackkkkerrrrrrrrank')
test.append('crackerhackerknar')
test.append('hhhackkerbanker')
#test = []
#test.append('rhackerank')
#test.append('hhhackkerbanker')
for t in test:
    print(t,hackerrankInString(t))


