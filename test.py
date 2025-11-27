import string

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

print(caesarCipher("okffng-Owvb", 2))