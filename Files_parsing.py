import os
import time

path = '/home/yauhen/'
list = []
for address, dirs, files in os.walk(path):
    for file in files:
        full = os.path.join(address, file)
        if time.time() - os.path.getctime(full) < 86400:
            list.append((full))
print(list)