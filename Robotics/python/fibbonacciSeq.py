# Calculate the 50th fib term
def fibonacci(n):
    a = 0
    b = 1
    if n < 0:
        raise("Error, fib only works w the positive terms")
    elif n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(2, n+1):
            c = a + b
            a = b
            b = c
        return b
print(fibonacci(50))