from collections import deque


def solution(num_list, n):
    q = deque(num_list)
    cnt = 0
    result = []
    tmp = []
    while q:
        tmp.append(q.popleft())
        cnt += 1
        if cnt == n:
            result.append(tmp)
            tmp = []
            cnt = 0

    return result