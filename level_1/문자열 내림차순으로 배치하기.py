def solution(s):
    answer = ''
    l = list(map(str,s))
    l.sort(reverse=True)
    for i in range(len(s)):
        answer += l[i]
    return answer
