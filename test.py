def misereNim(s):
    all_1s = True
    for i in s:
        if i > 1:
            all_1s = False
            break
    if all_1s:
        if len(s) % 2 == 0:
            return 'First'
        else:
            return 'Second'
    else:
        xor_sum = 0
        for i in s:
            xor_sum ^= i
        if xor_sum == 0:
            return 'Second'
        else:
            return 'First'


if __name__ == '__main__':
    s = [1, 1]
    s = [2, 1, 3]
    print(misereNim(s))