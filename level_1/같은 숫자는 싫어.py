def solution(arr):
    answer = []
    for i in range(len(arr)-1):
        if arr[i]==arr[i+1]:
            arr[i] = ''
        else:
            continue
    for i in range(len(arr)):
        if arr[i] != '':
            answer.append(arr[i])
    return answer
