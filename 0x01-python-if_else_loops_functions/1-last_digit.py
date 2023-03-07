#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
mid = str(number)[-1]
sign = "-" if number < 0 and int(mid) != 0 else ""
nb = -int(mid) if number < 0 else int(mid)
end = "and is greater than 5" if nb > 5 else "and is less than 6"


print(f"Last digit of {number} is {nb} {end}")
