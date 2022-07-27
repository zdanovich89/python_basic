array = [9, 8, 5, 6, 6, 9, 5, 2, 1, 6]


new_array = []
for x in array:
    new_array.append(x*2)


new_array2 = [x*3 for x in array]
z = {x*4 for x in array}
f = {x: x*5 for x in array}
g = [x for x in array if x % 2 == 0]

print(array)
print(new_array)
print(new_array2)
print(z)
print(f)
print(g)