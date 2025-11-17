#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superReducedString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

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

if __name__ == '__main__':

    ls = ["aabccddd","aaabccddd","aaabccddd","baab","aa","ab","aabbccddeeff","abcdeffedcba","aaabccba"]
    #print(set(s))

    for s in ls:
        result = superReducedString(s)
        print(result)
    
    s = "saveChangesInTheEditor"
    count = sum(1 for char in s if char.isupper())
    print(count + 1)

    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"

    pwd = "Ab1"
    has_number = any(char in numbers for char in pwd)
    has_lower = any(char in lower_case for char in pwd)
    has_upper = any(char in upper_case for char in pwd)
    has_special = any(char in special_characters for char in pwd)   
 
    s = 4 - (has_number + has_lower + has_upper + has_special)

    if s + len(pwd) >= 6:
        print(6 - len(pwd))
    else:
        print(s)
