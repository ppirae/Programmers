def solution(n, t):
    global cnt
    cnt = 0

    def dfs(L, sum):
        global cnt
        if L == len(n):
            if sum == t:
                cnt += 1
            return
        else:
            dfs(L + 1, sum + n[L])
            dfs(L + 1, sum - n[L])

    dfs(0, 0)
    return cnt