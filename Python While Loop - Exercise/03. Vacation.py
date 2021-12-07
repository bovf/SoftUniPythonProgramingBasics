money_needed = float(input())
money_saved = float(input())

days_counter = 0
spend_days_counter = 0
commands = ["save", "spend"]
while True:
    command = str(input())
    amount = float(input())
    if command == "save":
        money_saved += amount
        days_counter += 1
        spend_days_counter = 0
    if command == "spend":
        if money_saved >= amount:
            money_saved -= amount
        else:
            money_saved = 0
        days_counter += 1
        spend_days_counter += 1
    if command not in commands:
        break
    if money_saved >= money_needed:
        print(f"You saved the money for {days_counter} days.")
        break
    if spend_days_counter >= 5:
        print(f"You can't save the money."
              f"\n{days_counter}")
        break
