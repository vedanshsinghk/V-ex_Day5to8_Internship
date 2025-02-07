x = lambda a: a + 10
print(x(5))

x = lambda a: a+10
print(x(5))


x = lambda a, b: a * b
print(x(5, 6))

x=lambda a,b: a*b
print(x(5,6))



def myfunc(n):
    return lambda a: a * n

mydoubler = myfunc(2)
print(mydoubler(11))

def func(n):
    return lambda a: a*n
x=func(2)
print(x(11))