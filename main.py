import os
os.chdir('abc')

for i in range(1, 20001):
    os.mkdir(str(i))