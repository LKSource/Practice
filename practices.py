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