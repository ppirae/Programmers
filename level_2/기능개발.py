def solution(p, s):
    day = []
    for i in range(len(p)):
        tmp = 1
        while p[i] + s[i] * tmp < 100:
            tmp += 1
        day.append(tmp)

    res = []
    cnt = 1
    max = day[0]
    for i in range(1, len(day)):
        if day[i] > max:
            max = day[i]
            res.append(cnt)
            cnt = 1
        else:
            cnt += 1
        if i == len(day) - 1:
            res.append(cnt)
    return res