n = int(input())
evens = list()

for a in range(0, n+1):
    if a % 2 == 0:
        evens.append(a)

power = int
for e in evens:
    power = pow(2, e)
    print(power)
