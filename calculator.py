def add(x, y):
    return x+y

def factorial(n):
    p = 1
    for i in range(1, n+1):
        p = p * i
    return p

def sin(x, N):
    s = 0
    for n in range(N+1):
        s += (-1)**n * x**(2*n + 1)/factorial(2*n + 1)
    return s

def divide(x, y):
    return x/y

def square(x):
    return x**2

def squareroot(x):
    return x**0.5
