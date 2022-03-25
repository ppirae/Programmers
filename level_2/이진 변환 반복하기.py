def remove(s):
    s = s.replace("0", "")
    return s

def change(s, q):
    rev_base = ''

    while s > 0:
        s, mod = divmod(s, q)
        rev_base += str(mod)

    return rev_base[::-1]

def solution(s):
    zero_sum = 0
    change_sum = 0
    while s != "1":
        zero_cnt = s.count("0")
        zero_sum += zero_cnt
        s = len(remove(s))
        s = str(change(s, 2))
        change_sum += 1
    return [change_sum, zero_sum]
