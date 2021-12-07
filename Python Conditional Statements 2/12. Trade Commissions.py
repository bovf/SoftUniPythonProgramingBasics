city = str(input())
value = float(input())


commission = 0

if 0 <= value <= 500 and city == "Sofia":
    commission = value * 0.05
elif 500 < value <= 1000 and city == "Sofia":
    commission = value * 0.07
elif 1000 < value <= 10000 and city == "Sofia":
    commission = value * 0.08
elif value > 10000 and city == "Sofia":
    commission = value * 0.12
elif 0 <= value <= 500 and city == "Varna":
    commission = value * 0.045
elif 500 < value <= 1000 and city == "Varna":
    commission = value * 0.075
elif 1000 < value <= 10000 and city == "Varna":
    commission = value * 0.1
elif value > 10000 and city == "Varna":
    commission = value * 0.13
elif 0 <= value <= 500 and city == "Plovdiv":
    commission = value * 0.055
elif 500 < value <= 1000 and city == "Plovdiv":
    commission = value * 0.08
elif 1000 < value <= 10000 and city == "Plovdiv":
    commission = value * 0.12
elif value > 10000 and city == "Plovdiv":
    commission = value * 0.145

valid = (city == "Sofia" or city == "Varna" or city == "Plovdiv") \
        and value > 0

if not valid:
    print("error")
else:
    print(f"{commission:.2f}")
