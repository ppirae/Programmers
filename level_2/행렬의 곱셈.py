def solution(arr1, arr2):
    ROW = len(arr1)
    COL = len(arr2[0])
    arr2_ROW = len(arr2)

    answer = [[0 for j in range(COL)] for i in range(ROW)]
    for i in range(ROW):
        for j in range(COL):
            for k in range(arr2_ROW):
                answer[i][j] += arr1[i][k] * arr2[k][j]

    return answer