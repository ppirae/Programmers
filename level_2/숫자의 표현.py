def solution(n):
    start = 1
    end = 1
    sum = 1
    cnt = 1

    while end != n:
        if sum == n:
            cnt += 1
            end += 1
            sum += end
        elif sum > n:
            sum -= start
            start += 1
        elif sum < n:
            end += 1
            sum += end

    return cnt