import time

start_time = time.time()

sum_of_square = 0
sum = 0

for x in range(1, 101):
    sum_of_square += x**2
    sum += x

print(f"Sum of square = {sum_of_square}\n Square of sum = {sum**2}\n Them difference = {sum**2 - sum_of_square}")
print(f"Elapsed time: {time.time() - start_time} seconds")