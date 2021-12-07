budget = int(input())
season = str(input())
fishermen = int(input())

boat_price = 0
if season == "Spring":
    boat_price = 3000
elif season == "Summer":
    boat_price =4200
elif season == "Autumn":
    boat_price = 4200
elif season == "Winter":
    boat_price = 2600
total_cost = 0
if fishermen <= 6:
    total_cost = boat_price - boat_price * 0.1
elif 6 < fishermen <= 11:
    total_cost = boat_price - boat_price * 0.15
elif fishermen > 11:
    total_cost = boat_price - boat_price * 0.25

final_cost = 0
autumn_check = season == "Autumn"
if fishermen % 2 == 0 and not autumn_check:
    final_cost = total_cost - total_cost * 0.05
else:
    final_cost = total_cost

if budget >= final_cost:
    print(f"Yes! You have {(budget - final_cost):.2f} leva left.")
elif budget < final_cost:
    print(f"Not enough money! You need {abs(budget - final_cost):.2f} leva.")
