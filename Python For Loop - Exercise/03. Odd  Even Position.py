n = int(input())

numbers_list = list()
number_list_even = list()
number_list_odd = list()
number_counter = 1
count_even = 0
count_odd = 0
odd_min = 0
odd_max = 0
even_min = 0
even_max = 0
odd_sum = 0
even_sum = 0

for a in range(0, n):
    number = float(input())
    numbers_list.append(number)
    if number_counter % 2 != 0:
        number_list_odd.append(number)
        count_odd += 1
        odd_sum += number
    else:
        number_list_even.append(number)
        count_even += 1
        even_sum += number

    number_counter += 1

if count_even > 0:
    even_min = number_list_even[0]
    even_max = number_list_even[0]
    for i in number_list_even:
        if i >= even_max:
            even_max = i
        if i <= even_min:
            even_min = i

if count_odd > 0:
    odd_max = number_list_odd[0]
    odd_min = number_list_odd[0]
    for i in number_list_odd:
        if i >= odd_max:
            odd_max = i
        if i <= odd_min:
            odd_min = i

print(f"OddSum={odd_sum:.2f},")
if count_odd > 0:
    print(f"OddMin={odd_min:.2f},")
    print(f"OddMax={odd_max:.2f},")
else:
    print(f"OddMin=No,")
    print(f"OddMax=No,")
print(f"EvenSum={even_sum:.2f},")
if count_even > 0:
    print(f"EvenMin={even_min:.2f},")
    print(f"EvenMax={even_max:.2f}")
else:
    print(f"EvenMin=No,")
    print(f"EvenMax=No")

