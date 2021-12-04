def solution(n):
    answer = 0
    result = []
    for i in range(2, 999999):
        if n % i == 1:
            result.append(i);
            
    answer = min(result)
    return answer