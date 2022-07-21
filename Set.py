import time


def f(*args):
    list_new = []
    for i in args:
        for y in i:
            if y not in i:
                list_new.append(y)
    return list_new


z = list(range(10000))
x = list(range(5000, 15000))
c = list(range(10000, 20000))


start = time.time()
f(z, x, c)
stop = time.time() - start
print(stop)


start2 = time.time()
r = set(z)
t = r.union(set(x), set(c))
stop2 = time.time() - start2
print(stop2)


a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6, 7}

a.add(6)
a.discard(3)
m = a.intersection(b)
n = a.difference(b)

print(a)
print(m)
print(n)

text = open('/home/yauhen/Documents/memory.txt', encoding='latin-1')
t1 = set(text.read().split())
text.close()

text = open('/home/yauhen/Documents/text.txt', encoding='latin-1')
t2 = set(text.read().split())
text.close()

new = t1.difference(t2)
print(new)



