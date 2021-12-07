n = int(input())

numbers = list()
sum_numbers = 0
for a in range(0, n):
    number = int(input())
    numbers.append(number)
    sum_numbers += number

max_number = numbers[0]
sum_others = 0
number_equal_sum = 0
number_equal_sum_bool = False
for i in numbers:
    if i == sum_numbers - i:
        number_equal_sum_bool = i == sum_numbers - i
        number_equal_sum = i
    elif i >= max_number:
        max_number = i
        sum_others = sum_numbers - i

if number_equal_sum_bool:
    print(f"Yes"
          f"\nSum = {number_equal_sum}")
else:
    print(f"No"
          f"\nDiff = {abs(max_number - sum_others)}")
