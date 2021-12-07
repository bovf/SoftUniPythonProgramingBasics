number_locations = int(input())

for location in range(number_locations):
    expected_average = float(input())
    days_on_location = int(input())
    days_spent = 0
    gold_total = 0
    while days_spent < days_on_location:
        gold_mined = float(input())
        gold_total += gold_mined
        days_spent += 1

    location_average = gold_total / days_on_location
    if location_average >= expected_average:
        print(f"Good job! Average gold per day: {location_average:.2f}.")
    else:
        print(f"You need {(abs(location_average - expected_average)):.2f} gold.")
