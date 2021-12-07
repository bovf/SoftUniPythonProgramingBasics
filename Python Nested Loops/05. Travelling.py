while True:
    entry = input()
    if entry == "End":
        break
    money_needed = float(input())
    money_collected = 0
    deposit_entry = 0
    end_reached = False
    while True:
        if money_collected >= money_needed:
            print(f"Going to {entry}!")
            break
        entry2 = (input())
        if entry2 == "End":
            end_reached = True
            break
        deposit_entry = float(entry2)
        money_collected += deposit_entry
    if end_reached:
        break
