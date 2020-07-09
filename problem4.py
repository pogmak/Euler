
palindrome = 0

for i in range(100, 1000):
    for j in range(100, 1000):
        number = i * j
        if number == int("".join(list(reversed(str(number))))):
            if palindrome < number:
                palindrome = number

print(palindrome)