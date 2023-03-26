def sum(n):
    if n == 0:
        return 0
    else:
        return n+sum(n-1)

a = 50
b = sum(a)
print(b)