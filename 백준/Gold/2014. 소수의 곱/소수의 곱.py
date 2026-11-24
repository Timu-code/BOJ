import sys
import heapq

input = sys.stdin.readline

k, n = map(int, input().split())
array = list(map(int, input().split()))

h = array[:]

for _ in range(n):
    x = heapq.heappop(h)
    
    for p in array:
        if x * p >= 2 ** 31:
            break
        
        heapq.heappush(h, x * p)
        
        if x % p == 0:
            break

print(x)