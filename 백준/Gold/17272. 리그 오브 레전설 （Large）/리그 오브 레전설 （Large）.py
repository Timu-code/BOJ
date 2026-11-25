import sys

input = sys.stdin.readline

n, m = map(int, input().split())
mod = 1000000007

t = [[0] * m for _ in range(m)]
t[0][0] += 1
t[0][m - 1] += 1

for i in range(1, m):
    t[i][i - 1] = 1

r = [[int(i == j) for j in range(m)] for i in range(m)]

while n:
    if n % 2:
        r = [[sum(a * b for a, b in zip(x, y)) % mod for y in zip(*t)] for x in r]
        
    t = [[sum(a * b for a, b in zip(x, y)) % mod for y in zip(*t)] for x in t]
    n //= 2

print(r[0][0])