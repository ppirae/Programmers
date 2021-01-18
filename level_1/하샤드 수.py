def solution(x):
    answer = True
    x1 = list(map(int,str(x)))
    if x % sum(x1) == 0:
        answer = True
    else:
        answer = False
    return answer
