def solution(arr):
    import math

    def lcm(an, bn):
        return (an * bn) // math.gcd(an, bn)

    n = arr[0]
    for i in range(1, len(arr)):
        n = lcm(n, arr[i])

    return n