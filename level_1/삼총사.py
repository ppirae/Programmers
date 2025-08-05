from itertools import combinations
def solution(number):
    answer = 0
    sum = 0
    for i in combinations(number, 3):
        for j in i:
            sum += j
        if sum == 0:
            answer += 1
        sum = 0
    return answer