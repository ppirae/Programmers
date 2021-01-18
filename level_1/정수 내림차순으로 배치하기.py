def solution(n):
    result = ''
    answer = 0
    n = list(map(int,str(n)))
    n.sort(reverse=True)
    for i in range(len(n)):
        result += str(n[i])
        answer = int(result)
    return answer
