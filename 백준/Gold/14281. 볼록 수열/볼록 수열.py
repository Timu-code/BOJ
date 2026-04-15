import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
result = 0

while True:
    flag = True
    
    for i in range(1, n - 1):
        if a[i - 1] + a[i + 1] < 2 * a[i]:
            tmp = a[i] - (a[i - 1] + a[i + 1]) // 2
            a[i] -= tmp
            result += tmp
            flag = False
            
    if flag:
        break

print(result)