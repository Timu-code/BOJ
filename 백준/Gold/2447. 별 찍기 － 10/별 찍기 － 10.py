def draw_stars(n):
    if n == 1:
        return ['*']
    
    prev = draw_stars(n // 3)
    stars = []
    
    for line in prev:
        stars.append(line * 3)
        
    for line in prev:
        stars.append(line + ' ' * (n // 3) + line)
        
    for line in prev:
        stars.append(line * 3)
        
    return stars

n = int(input())
print('\n'.join(draw_stars(n)))