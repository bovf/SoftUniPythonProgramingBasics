budget = float(input())
number_of_extras = int(input())
price_of_costumes_per_extra = float(input())

cost_of_decoration = budget * 0.1
if number_of_extras > 150:
    cost_of_costumes = number_of_extras * price_of_costumes_per_extra * 0.9
else:
    cost_of_costumes = number_of_extras * price_of_costumes_per_extra

total_cost = cost_of_costumes + cost_of_decoration

if total_cost > budget:
    print("Not enough money!")
    print(f"Wingard needs {abs(budget - total_cost):.2f} leva more.")
elif total_cost <= budget:
    print ("Action!")
    print (f"Wingard starts filming with {abs (budget - total_cost):.2f} leva left.")