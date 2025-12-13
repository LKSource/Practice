import itertools

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

g = [['ebacd', 'fghij', 'olman', 'trpqs', 'xywuv']]
for i in g:
    print(gridChallenge(i))

'''
    print(tl)
    for i in range(len(grid)):
        for j in range(1, len(grid)):
#            print( grid[j][i], grid[j-1][i])
            if grid[j][i] < grid[j-1][i]:
                check = False
                break
'''