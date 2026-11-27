import sys

input = sys.stdin.readline

a, b = map(int, input().split())
b += 1

result = 0
half = 1

while half <= b:
    cycle = half * 2
    result += (b // cycle - a // cycle) * half
    result += max(0, b % cycle - half) - max(0, a % cycle - half)
    half *= 2

print(result)