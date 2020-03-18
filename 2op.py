def broken_device(x, y):
    ans = 0
    while y != x:
        if (y > x) and (2*(x-1) != y):
            x *= 2
        else: 
            x -= 1
        ans += 1
    return ans
    
x = 5
y = 8
print(broken_device( x, y ))