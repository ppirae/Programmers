def solution(left, right):
    answer = 0
    cnt = 0
    result_odd = []
    result_even = []
    
    for i in range(left, right+1):
        for j in range(1, i+1):
            if i%j == 0:
                cnt += 1
        print(cnt)
        if cnt%2==0:
            result_even.append(j)
            cnt = 0
        else:
            result_odd.append(j)
            cnt = 0
    answer = sum(result_even) - sum(result_odd)
    return answer