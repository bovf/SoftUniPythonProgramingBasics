n = int(input())

p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0
p1_list = list()
p2_list = list()
p3_list = list()
p4_list = list()
p5_list = list()
number_counter = 0
p1_list_counter = 0
p2_list_counter = 0
p3_list_counter = 0
p4_list_counter = 0
p5_list_counter = 0

for a in range(0, n):
    number = int(input())
    number_counter += 1
    if number < 200:
        p1_list.append(number)
        p1_list_counter += 1
    elif 200 <= number < 400:
        p2_list.append(number)
        p2_list_counter += 1
    elif 400 <= number < 600:
        p3_list_counter += 1
        p3_list.append(number)
    elif 600 <= number < 800:
        p4_list_counter += 1
        p4_list.append(number)
    elif number >= 800:
        p5_list.append(number)
        p5_list_counter += 1

p1 = p1_list_counter / number_counter * 100
p2 = p2_list_counter / number_counter * 100
p3 = p3_list_counter / number_counter * 100
p4 = p4_list_counter / number_counter * 100
p5 = p5_list_counter / number_counter * 100

print(f"{p1:.2f}%")
print(f"{p2:.2f}%")
print(f"{p3:.2f}%")
print(f"{p4:.2f}%")
print(f"{p5:.2f}%")
