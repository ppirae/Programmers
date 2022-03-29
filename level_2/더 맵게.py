import heapq

def solution(a, K):
    heapq.heapify(a)

    cnt = 0
    while len(a) >= 2:
        min_ = heapq.heappop(a)
        if min_ >= K:
            return cnt

        else:
            min_2 = heapq.heappop(a)
            heapq.heappush(a, min_ + (min_2 * 2))
            cnt += 1

    if a[0] > K:
        return cnt
    else:
        return -1