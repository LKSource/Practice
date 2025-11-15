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
