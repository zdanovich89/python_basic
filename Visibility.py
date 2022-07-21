import math

PI = math.pi


def radius():
    n = float(input('Cylinder diameter in sm: '))
    n /= 2
    return n


def height():
    m = float(input('Cylinder height in sm: '))
    return m


def volume():
    r = radius()
    h = height()
    s = PI*r**2
    v = s*h
    return v


print('Cylinder volume: ', volume(), 'sm3')


def weight(g):
    n = float(input('Cylinder weight g/sm3: '))
    return g*n/1000


print('Cylinder weight in kg: ', weight(volume()))