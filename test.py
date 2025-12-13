import itertools

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

n = 6
k = 3
contests = [[5, 1], [2, 1], [1, 1], [8, 1], [10, 0], [5, 0]]
print(luckBalance(k,contests))