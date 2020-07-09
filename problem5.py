import time

start_time = time.time()

list_divider = [11, 13, 14, 16, 17, 18, 19, 20]

for number in range(20, 99999999999999, 20):
    if all(number % i == 0 for i in list_divider):
        break

print(number)
print(f"Elapsed time: {time.time() - start_time}")
