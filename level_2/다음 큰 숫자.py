def solution(n):
    answer = 0
    num_1 = (list(map(int,str(bin(n))[2:]))).count(1)

    for i in range(n+1, 1000001):
        num_2 = (list(map(int,str(bin(i))[2:]))).count(1)
        if num_2 == num_1:
            answer = i
            break
    return answer
