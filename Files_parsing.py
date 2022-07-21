import os

path = '/home'
list_path = []
for address, dirs, files in os.walk(path):
    for file in files:
        full_path = os.path.join(address, file)
        list_path.append(full_path)


#r = open('paths.txt', 'w')
#for x in list_path:
#    r.write(x + '\n')
r = open('paths.txt')
for i in r:
    if 'read.py' in i:
        print(i)

r.close()