def solution(my_string, s, e):
    answer = ''
    r_string = my_string[s:e+1]
    r_string = r_string[::-1]
    a = my_string[0:s]
    b = my_string[e+1:]
    answer = a + r_string + b
    return answer