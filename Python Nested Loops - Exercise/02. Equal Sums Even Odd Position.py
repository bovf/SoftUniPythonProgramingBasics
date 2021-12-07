n1 = int(input())
n2 = int(input())

for i in range(n1, n2+1):
    sum_odd = 0
    sum_even = 0
    for index, value in enumerate(str(i)):
        if (index + 1) % 2 == 0:
            sum_even += int(value)
        if (index + 1) % 2 != 0:
            sum_odd += int(value)
    if sum_odd == sum_even:
        print(f"{i} ", end ="")
