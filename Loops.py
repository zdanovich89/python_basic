for x in range(0, 10 + 1):
    print(x)

y = 0

while True:
    print(y)
    y = y + 1
    if y == 10:
        break

# alphabet = "abcdefghijklmnoprstuvwyz"
# text = input("Enter text: \n")
#
# for i in alphabet:
#     count = 0
#     for letter in text:
#         if i == letter:
#             count += 1
#     if count > 0:
#         print("Letter " + i.upper() + " " + str(count) + " times")

n = list(range(10))
m = []
for i in n:
    if i == 2 or i == 4:
        continue
    m += [i]

else:
    print(m)

n = list(range(1, 21))
m = []

for i in n:
    if i % 2 == 0:
        m.append(i)
        n.remove(i)
else:
    print(m)
    print(n)