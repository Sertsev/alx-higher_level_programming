#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number > 0:
    div = 10
else:
    div = -10

quot = number % div

print(f"Last digit of {number} is {quot} and is ", end="")

if quot > 5:
    print("greater than 5")
elif quot == 0:
    print("0")
elif quot < 6 and quot != 0:
    print("less than 6 and not 0")
