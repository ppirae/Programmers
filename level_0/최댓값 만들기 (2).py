def solution(numbers):
    answer = 0
    numbers.sort()
    minus = numbers[0] * numbers[1]
    plus = numbers[-1] * numbers[-2]
    if minus > plus:
        answer = minus
    elif minus < plus:
        answer = plus
    else:
        answer = plus
    return answer