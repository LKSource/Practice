#!/bin/python3

import math
import os
import random
import re
import sys

def count_overlapping(text, pattern):
    if not pattern:
        return 0
    count = 0
    start = 0
    while True:
        pos = text.find(pattern, start)
        if pos == -1:
            break
        count += 1
        start = pos + 1  # Move by 1 for overlapping
    return count

if __name__ == '__main__':
    #n = int(input().strip())

    genes = "a b c aa d b".split()

    health = list(map(int, "1 2 3 4 5 6".split()))

    s = ["1 5 caaab", "0 4 xyz", "2 4 bcdybc"].copy()
    rslt = []

    for s_itr in range(3):
        first_multiple_input = s[s_itr].split()

        first = int(first_multiple_input[0])

        last = int(first_multiple_input[1])

        d = first_multiple_input[2]
        print(first, last, d)
        total = 0
        for i in range(first, last + 1):
            gene = genes[i]
            # Skip empty genes (though unlikely)
            if not gene:
                continue
            cnt = count_overlapping(d, gene)
            total += cnt * health[i]
        rslt.append(total)
    
    print(min(rslt), max(rslt))