def solution(strings, n):
    answer = []
    strings.sort()
    answer = sorted(strings, key = lambda s: s[n])
    return answer
