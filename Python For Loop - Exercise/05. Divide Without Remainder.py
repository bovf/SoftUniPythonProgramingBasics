n = int(input())

p1 = 0  # % 2 = 0
p2 = 0  # % 3 = 0
p3 = 0  # % 4 = 0
number_counter = 0
p1_list = list()
p2_list = list()
p3_list = list()
p1_list_counter = 0
p2_list_counter = 0
p3_list_counter = 0

for a in range(0, n):
    number = int(input())
    number_counter += 1
    if number % 2 == 0:
        p1_list.append(number)
        p1_list_counter += 1
    if number % 3 == 0:
        p2_list.append(number)
        p2_list_counter += 1
    if number % 4 == 0:
        p3_list.append(number)
        p3_list_counter += 1

p1 = p1_list_counter / number_counter * 100
p2 = p2_list_counter / number_counter * 100
p3 = p3_list_counter / number_counter * 100

print(f"{p1:.2f}%")
print(f"{p2:.2f}%")
print(f"{p3:.2f}%")