
remainder = 1
number = 0

while remainder != 0:
    number += 1
    for i in range(1,21):
        remainder = number % i
        if remainder != 0:
            break

print(number)
