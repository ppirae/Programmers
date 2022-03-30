from collections import deque

def solution(p, l):
    a = []
    for idx, prior in enumerate(p):
        a.append((idx, prior))

    a = deque(a)
    cnt = 0
    while True:
        tmp = a.popleft()
        if any(tmp[1] < x[1] for x in a):
            a.append(tmp)
        else:
            cnt += 1
            if tmp[0] == l:
                return cnt
                break