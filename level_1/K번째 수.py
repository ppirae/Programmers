def solution(array, commands):
    answer = []
    result = [[] for i in range(len(commands))]
    for i in range(len(commands)):
        for j in range(commands[i][0]-1, commands[i][1]):
            result[i].append(array[j])

    for i in range(len(result)):
        result[i].sort()

    for i in range(len(commands)):
        answer.append(result[i][commands[i][2]-1])

    return answer
