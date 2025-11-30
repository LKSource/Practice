import string
def gemstones(arr):
    # Write your code here
    ref = string.ascii_lowercase

    for s in arr:
        ref = ''.join([c for c in ref if c in s])
    #print(ref)
    return len(ref)

arr = ['abcdde', 'baccd', 'eeabgc']
print(gemstones(arr))  
