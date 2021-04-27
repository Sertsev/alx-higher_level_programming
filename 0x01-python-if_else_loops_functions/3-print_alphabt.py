#!/usr/bin/python3
for alphabet in range(ord('a'), ord('z')+1):
    if alphabet in [101, 113]:
        continue
    print("{:c}".format(alphabet), end="")
    
