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
