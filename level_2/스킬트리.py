from collections import deque
def solution(s, t):
    cnt = 0
    r = len(s)
    for st in t:
        dq = deque(s)
        for x in st:
            if x in dq:
                if x != dq.popleft():
                    break
        else:
            cnt += 1
    return cnt