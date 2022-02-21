import time
i = 0



max = 1000
st = time.time()
while i < max:
    i += 1
print(time.time() - st)

st = time.time()
for i in range(1000000):
    if i == max:
        break
print(time.time() - st)