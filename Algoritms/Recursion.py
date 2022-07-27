def say_Hello(x):
    if x == 0:
        return
    else:
        print("Hello World!!! " + str(x))
        say_Hello(x-1)


def sum(x):
    if x == 0:
        return 0
    else:
        return x + sum(x-1)


def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x-1)


def fibonacci(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return fibonacci(x-1) + fibonacci(x-2)


say_Hello(3)
z = sum(995)
print(z)
y = factorial(5)
print(y)
c = fibonacci(40)
print(c)
