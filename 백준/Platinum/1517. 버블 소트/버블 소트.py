n = int(input())
array = list(map(int, input().split()))
tmp = [0] * n
result = 0

w = 1
while w < n:
    for l in range(0, n, w * 2):
        m = min(l + w, n)
        h = min(l + w * 2, n)
        
        if m >= h:
            continue

        i, j, k = l, m, l
        
        while i < m and j < h:
            if array[i] <= array[j]:
                tmp[k] = array[i]; i += 1
            else:
                tmp[k] = array[j]; j += 1
                result += m - i
            k += 1
            
        while i < m:
            tmp[k] = array[i]; i += 1; k += 1
            
        while j < h:
            tmp[k] = array[j]; j += 1; k += 1
            
        array[l:h] = tmp[l:h]
    w *= 2

print(result)