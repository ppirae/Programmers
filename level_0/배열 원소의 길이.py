def solution(strlist):
    ans = []
    for i in strlist:
        ans.append(len(list(i)))
    return ans