def solution(n, a, b):
    if a % 2 != 0:
        a += 1
    if b % 2 != 0:
        b += 1

    cnt = 1
    while a != b:
        a //= 2
        b //= 2
        if a % 2 != 0:
            a += 1
        if b % 2 != 0:
            b += 1
        cnt += 1

    return cnt