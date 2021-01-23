def solution(a, b):
    answer = ''
    yoil = ["THU","FRI","SAT","SUN","MON","TUE","WED"]
    month = [0,31,29,31,30,31,30,31,31,30,31,30,31]
    total = 0
    for i in range(a):
        total += month[i]

    total += b
    c = total % 7
    answer =  yoil[c]
    return answer
