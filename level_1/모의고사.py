def solution(answers):
    answer = []
    arr_1 = [1, 2, 3, 4, 5]
    arr_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    arr_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    count = [0] * 3

    for i in range(len(answers)):
        if answers[i] == arr_1[i % 5]:
            count[0] += 1
        if answers[i] == arr_2[i % 8]:
            count[1] += 1
        if answers[i] == arr_3[i % 10]:
            count[2] += 1

    win = max(count)
    for i in range(len(count)):
        if count[i] == win:
            answer.append(i + 1)

    return answer