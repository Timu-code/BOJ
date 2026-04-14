import sys

input = sys.stdin.readline

c, d, m = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(c)]

for j in range(1, d):
    dp = [0] * (m + 1)

    for i in range(c):
        prev = array[i][j - 1]
        diff = array[i][j] - prev

        for k in range(prev, m + 1):
            dp[k] = max(dp[k], dp[k - prev] + diff)

    m += dp[m]

print(m)