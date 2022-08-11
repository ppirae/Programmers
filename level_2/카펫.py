def solution(brown, yellow):
    sum = brown + yellow
    yak = []
    for i in range(1, sum + 1):
        if sum % i == 0:
            yak.append(i)

    yak.reverse()
    start = 0
    end = len(yak) - 1
    while start <= end:
        left = yak[start]
        right = yak[end]
        left = left - 2
        right = right - 2
        if left <= 0 or right <= 0:
            pass
        else:
            if (left * right) == yellow:
                return [left + 2, right + 2]
                break
        start += 1
        end -= 1