import sys

input = sys.stdin.readline

s = input().rstrip()
n = len(s)
mod = 10007

dp = [[0] * n for _ in range(n)]

for i in range(n - 1, -1, -1):
    dp[i][i] = 1
    
    for j in range(i + 1, n):
        if s[i] == s[j]:
            dp[i][j] = (dp[i + 1][j] + dp[i][j - 1] + 1) % mod
            
        else:
            dp[i][j] = (dp[i + 1][j] + dp[i][j - 1] - dp[i + 1][j - 1]) % mod

print(dp[0][n - 1])