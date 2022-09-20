#다이나믹 프로그래밍
def solution(n):
    dp = [0 for _ in range(2001)]

    dp[0] = 0
    dp[1] = 1
    dp[2] = 2
    dp[3] = 3
    dp[4] = 5

    for i in range(5, 2001):
        dp[i] = dp[i - 1] + dp[i - 2]

    ans = dp[n] % 1234567
    return ans