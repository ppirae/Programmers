def solution(n):
    ans = 0
    if n%7==0:
        ans = n//7
    else:
        ans = (n//7) + 1
    return ans