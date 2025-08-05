def solution(num_list):
    answer = []
    result = 0
    last = num_list[-1]
    lastwo = num_list[-2]
    if last > lastwo:
        result = last - lastwo
    else:
        result = last * 2
    num_list.append(result)
    return num_list