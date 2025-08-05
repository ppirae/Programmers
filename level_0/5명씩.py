def solution(names):
    answer = []
    cnt = 5
    for i in range(len(names)):
        if i%5 == 0:
            answer.append(names[i])
    return answer