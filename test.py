from collections import Counter

MOD = 1000000007
MAX_N = 10**5 + 5

# Global
s = ""
fact = None
_fact_computed = False

def _precompute_factorials():
    global fact, _fact_computed
    if _fact_computed:
        return
    fact = [1] * MAX_N
    for i in range(1, MAX_N):
        fact[i] = (fact[i-1] * i) % MOD
    _fact_computed = True

def initialize(s_input):
    global s
    s = s_input
    _precompute_factorials()

def modinv(a, mod=MOD):
    return pow(a, mod - 2, mod)

def answerQuery(l, r):
    global s, fact
    if not s:
        raise ValueError("Call initialize(s) first.")
    
    substr = s[l-1:r]
    n = len(substr)
    freq = Counter(substr)
    
    # Build half multiset and count odd-frequency characters
    half_freq = []
    odd_count = 0
    half_len = 0
    for count in freq.values():
        half_len += count // 2
        if count % 2 == 1:
            odd_count += 1

    # Number of distinct permutations of the half
    numerator = fact[half_len]
    denominator = 1
    for count in freq.values():
        half_c = count // 2
        if half_c > 0:
            denominator = (denominator * fact[half_c]) % MOD

    half_perms = (numerator * modinv(denominator)) % MOD

    # Number of choices for center: max(1, odd_count)
    center_choices = odd_count if odd_count > 0 else 1

    result = (half_perms * center_choices) % MOD
    return result

# Step 1: Initialize with your string
initialize("week")

# Step 2: Answer queries (1-indexed)
print(answerQuery(1, 4))  # Output: 6
print(answerQuery(2, 3))  # Substring "bccb" → 2!/(1!*1!) = 2