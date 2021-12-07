n1 = int(input())
n2 = int(input())
sum = int(input())

sum_found = False
sum_number = 0
combination_counter = 0
first_number = int
second_number = int
for a1 in range(n1, n2+1):
    for a2 in range(n1, n2+1):
        combination_counter += 1
        if sum == a1 + a2:
            sum_found = True
            sum_number = combination_counter
            first_number = a1
            second_number = a2
            break
    if sum_found:
        break

if sum_found:
    print(f"Combination N:{sum_number} ({first_number} + {second_number} = {sum})")
else:
    print(f"{combination_counter} combinations - neither equals {sum}")