def solution(my_string):
    answer = ''
    check = []
    for i in my_string:
        if i in check:
            pass
        else:
            answer += i
            check.append(i)
    return answer