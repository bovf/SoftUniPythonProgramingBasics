import sys
n = int(input())

numbers_list = list()
for a in range(1, n+1):
    number = int(input())
    numbers_list.append(number)

# number_temp_greater = numbers_list[1]
# number_temp_less = numbers_list[1]
number_temp_greater = -sys.maxsize
number_temp_less = sys.maxsize
for a in numbers_list:
    if a >= number_temp_greater:
        number_temp_greater = a
    if a <= number_temp_less:
        number_temp_less = a
print(f"Max number: {number_temp_greater}")
print(f"Min number: {number_temp_less}")

#Не е правилно зададена задачата.