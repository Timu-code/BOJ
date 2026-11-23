import sys

input = sys.stdin.readline

n = int(input())

l = 1
count = 9

while n > l * count:
    n -= l * count
    l += 1
    count *= 10

print(str(10 ** (l - 1) + (n - 1) // l)[(n - 1) % l])