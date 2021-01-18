import math
def solution(n):
    answer = 0
    arr = []

    def is_prime_number(n):
        for i in range(2, int(math.sqrt(n))+1):
            if n%i == 0:
                return False
        return True

    for i in range(2, n+1):
        arr.append(is_prime_number(i))

    answer = arr.count(True)
    return answer
