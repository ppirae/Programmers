def solution(t, p):
    answer = 0
    length = len(p)
    start = 0
    end = start + length-1
    while end < len(t):
        temp = t[start:end+1]
        if int(temp) <= int(p):
            answer += 1
        start += 1
        end += 1
    return answer