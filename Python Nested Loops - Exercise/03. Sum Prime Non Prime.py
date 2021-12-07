prime_sum = 0
non_prime_sum = 0

while True:
    entry = input()
    if entry == "stop":
        break
    number = int(entry)
    if number == 1:
        prime_sum += number
    elif number == 0:
        non_prime_sum += number
    elif number == 2:
        prime_sum += number
    elif number > 1:
        for i in range(2, number):
            if number % i == 0:
                is_prime = False
                break
            else:
                is_prime = True

        if is_prime:
            prime_sum += number
        if not is_prime:
            non_prime_sum += number
    else:
        print("Number is negative.")

print(f"Sum of all prime numbers is: {prime_sum}")
print(f"Sum of all non prime numbers is: {non_prime_sum}")

