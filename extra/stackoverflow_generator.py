"""
Laptop go brr
"""
def ackermann(m, n):
    if m == 0:
        return (n + 1)
    elif n == 0:
        return ackermann(m - 1, 1)
    else:
        return ackermann(m - 1, ackermann(m, n - 1))


for x in range(5):
    for y in range(5):
        print(ackermann(x, y))