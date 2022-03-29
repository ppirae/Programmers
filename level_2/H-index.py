def solution(c):
    h = 0
    while True:
        cnt = 0
        for i in c:
            if i > h:
                cnt += 1
        if cnt > h:
            h += 1
        else:
            return h