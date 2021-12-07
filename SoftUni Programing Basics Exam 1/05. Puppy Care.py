food_grams = int(input()) * 1000

food_ate = 0
while True:
    daily_entry = input()
    if daily_entry == "Adopted":
        break
    else:
        food_ate += int(daily_entry)

if food_ate > food_grams:
    print(f"Food is not enough. You need {(abs(food_grams - food_ate)):.0f} grams more.")
else:
    print(f"Food is enough! Leftovers: {(abs(food_grams - food_ate)):.0f} grams.")
