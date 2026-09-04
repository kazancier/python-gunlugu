"""

counter = 5
while counter < 10:

    print(counter)
    counter += 1
    if counter == 6:
        continue
    print(counter)
    print("zzz")

"""
"""
i = 0
while i < 6:
    break
    print(i)
    i = i + 1

"""
"""
for i in range(1,7):
    print('zzz')
   
    print(i)
"""
import random, sys

z = 0
for i in range(101):
    z+=i
    if i == 50:
        sys.exit()
print(z)