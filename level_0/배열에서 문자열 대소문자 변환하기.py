def solution(strArr):
    answer = []
    idx = 0
    for i in strArr:
        if idx%2 != 0:
            answer.append(i.upper())
        else:
            answer.append(i.lower())
        idx += 1
    return answer