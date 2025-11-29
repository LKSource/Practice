import string
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

arr ="We promptly judged antique ivory buckles for the next prize"
print(pangrams(arr))