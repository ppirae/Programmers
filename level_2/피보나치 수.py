import sys
sys.setrecursionlimit(10**7)

def solution(x):
    d = [0] * 100002
    d[0] = 0
    d[1] = 1
    d[2] = 1

    for i in range(3, x+1):
        d[i] = d[i-1] + d[i-2]
    return d[x]%1234567
