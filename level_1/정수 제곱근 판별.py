import math

def solution(n):
    answer = 0
    if math.sqrt(n)-int(math.sqrt(n))==0:
        answer = (math.sqrt(n)+1)**2
    else:
        return 'no'
    return answer
