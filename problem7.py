import time

start_time = time.time()

need_amount = 10001
amount = 0
i = 2
while amount != need_amount:
    j = 2
    brk = False
    while j < i:
        if i % j == 0:
            brk = True
            break
        j += 1
    if not brk:
        print(i)
        amount += 1
    i += 1

print(f"Elapsed time: {time.time() - start_time} seconds")
