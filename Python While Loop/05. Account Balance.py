sum_total = 0
while True:
    entry = input()
    if entry == "NoMoreMoney" or entry == "0" or entry == "":
        print(f"Total: {sum_total:.2f}")
        break
    if float(entry) < 0:
        print (f"Invalid operation!")
        print (f"Total: {sum_total:.2f}")
        break
    sum_total += float(entry)
    print(f"Increase: {float(entry):.2f}")
