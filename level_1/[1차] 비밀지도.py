def solution(n, arr1, arr2):
    for i in range(len(arr1)):
        arr1[i] = str(bin(arr1[i]))[2:]
        while len(arr1[i]) != len(arr1):
            arr1[i] = (arr1[i][::-1]+'0')[::-1]

    for i in range(len(arr2)):
        arr2[i] = str(bin(arr2[i]))[2:]
        while len(arr2[i]) != len(arr2):
            arr2[i] = (arr2[i][::-1]+'0')[::-1]

    for i in range(len(arr1)):
        arr1[i] = list(arr1[i])
        arr2[i] = list(arr2[i])

    for i in range(len(arr1)):
        for j in range(len(arr1)):
            arr1[i][j] = int(arr1[i][j]) | int(arr2[i][j])

    for i in range(len(arr1)):
        for j in range(len(arr1)):
            if arr1[i][j] == 1:
                arr1[i][j] = "#"
            else:
                arr1[i][j] = " "

    for i in range(len(arr1)):
        arr1[i] = ''.join(arr1[i])

    return arr1
