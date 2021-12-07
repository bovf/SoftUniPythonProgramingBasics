n1 = int(input())
n2 = int(input())
operator = str(input())

operators_list = ["+", "-", "*", "/", "%"]
even_or_odd_list = ["even", "odd"]
operator_counter = 0
for a in operators_list:
    if operator == a:
        break
    else:
        operator_counter += 1

even_or_odd_placeholder = str
result = 0
if operator_counter == 0 or operator_counter == 1 or operator_counter == 2:
    if operator_counter == 0:
        result = n1 + n2
    elif operator_counter == 1:
        result = n1 - n2
    elif operator_counter == 2:
        result = n1 * n2
    if result % 2 == 0:
        even_or_odd_placeholder = even_or_odd_list[0]
    else:
        even_or_odd_placeholder = even_or_odd_list[1]
    print(f"{n1} {operator} {n2} = {result} - {even_or_odd_placeholder}")

elif operator_counter == 3:
    if n2 != 0:
        result = n1 / n2
        print(f"{n1} / {n2} = {result:.2f}" )
    else:
        print(f"Cannot divide {n1} by zero")
elif operator_counter == 4:
    if n2 != 0:
        result = n1 % n2
        print(f"{n1} % {n2} = {result}" )
    else:
        print(f"Cannot divide {n1} by zero")
