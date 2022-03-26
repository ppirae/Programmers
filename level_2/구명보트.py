from collections import deque
def solution(a, m):
    a.sort(reverse=True)
    a = deque(a)

    cnt = 0
    while a:
        if len(a) == 1:
            cnt += 1
            break
        if a[0] + a[-1] <= m:
            a.popleft()
            a.pop()
        else:
            a.popleft()
        cnt += 1
    return cnt