def solution(num, k):
    num = list(map(int, str(num)))
    if k in num:
        return num.index(k) + 1
    else:
        return -1