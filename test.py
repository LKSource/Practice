
from collections import defaultdict

def sherlockAndAnagrams(s):
    # Write your code here
    n = len(s)
    total_pairs = 0

    # Iterate over all possible substring lengths (1 to n-1)
    for length in range(1, n):
        freq_map = defaultdict(int)
        
        # Extract all substrings of current length
        for i in range(n - length + 1):
            substring = s[i:i + length]
            # Sort characters to create anagram signature
            sorted_sub = ''.join(sorted(substring))
            freq_map[sorted_sub] += 1
        
        # For each anagram group, count pairs: C(count, 2)
        for count in freq_map.values():
            if count > 1:
                total_pairs += count * (count - 1) // 2

    return total_pairs

s = 'abba'
s = 'cdcd'
s = 'kkkk'
#s = 'abc'
print(sherlockAndAnagrams(s))