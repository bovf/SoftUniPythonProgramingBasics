flowers_type = str(input())
quantity_flowers = int(input())
budget = int(input())

flowers = ["Roses", "Dahlias", "Tulips", "Narcissus", "Gladiolus"]
prices_flowers = [5, 3.8, 2.8, 3, 2.5]


counter_for1 = 0
for a in flowers:
    if flowers_type == a:
        break
    else:
        counter_for1 += 1
    if counter_for1 == 4:
        break

price = (prices_flowers[counter_for1])

total_cost = 0
if flowers_type == "Roses" and quantity_flowers > 80:
    total_cost = price * quantity_flowers
    total_cost -= total_cost * 0.1
elif flowers_type == "Dahlias" and quantity_flowers > 90:
    total_cost = price * quantity_flowers
    total_cost -= total_cost * 0.15
elif flowers_type == "Tulips" and quantity_flowers > 80:
    total_cost = price * quantity_flowers
    total_cost -= total_cost * 0.15
elif flowers_type == "Narcissus" and quantity_flowers < 120:
    total_cost = price * quantity_flowers
    total_cost += total_cost * 0.15
elif flowers_type == "Gladiolus" and quantity_flowers < 80:
    total_cost = price * quantity_flowers
    total_cost += total_cost * 0.20
else:
    total_cost = price * quantity_flowers

if budget >= total_cost:
    print(f"Hey, you have a great garden with"
          f" {quantity_flowers} {flowers_type} "
          f"and {(budget - total_cost):.2f} leva left.")
elif budget < total_cost:
    print(f"Not enough money, you need "
          f"{(abs(budget - total_cost)):.2f} "
          f"leva more.")
