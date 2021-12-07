budget = float(input())
season = str(input())

destinations = ["Bulgaria", "Balkans", "Europe"]
seasons = ["summer", "winter"]
accommodation = ["Camp", "Hotel"]
counter_season = 0
#0 = summer
#1 = winter
for a in seasons:
    if a == season:
        break
    else:
        counter_season += 1

holiday_destination = str
holiday_accommodation = str
money_spent = 0
if budget <= 100:
    holiday_destination = destinations[0]
    if counter_season == 0:
        money_spent = budget * 0.3
        holiday_accommodation = accommodation[0]
    elif counter_season == 1:
        money_spent = budget * 0.7
        holiday_accommodation = accommodation[1]
elif 100 < budget <= 1000:
    holiday_destination = destinations[1]
    if counter_season == 0:
        holiday_accommodation = accommodation[0]
        money_spent = budget * 0.4
    elif counter_season == 1:
        holiday_accommodation = accommodation[1]
        money_spent = budget * 0.8
elif 1000 < budget:
    holiday_destination = destinations[2]
    money_spent = budget * 0.9
    holiday_accommodation = accommodation[1]

print(f"Somewhere in {holiday_destination}")
print(f"{holiday_accommodation} - {money_spent:.2f}")