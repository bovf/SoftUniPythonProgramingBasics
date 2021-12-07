price_of_strawberries = float (input ())
quantity_of_bananas_kg = float (input ())
quantity_of_oranges_kg = float (input ())
quantity_of_raspberries_kg = float (input ())
quantity_of_strawberries_kg = float (input ())

price_of_raspberries = price_of_strawberries / 2
price_of_oranges = price_of_raspberries - price_of_raspberries * 0.4
price_of_bananas = price_of_raspberries - price_of_raspberries * 0.8

cost_of_strawberries = price_of_strawberries * quantity_of_strawberries_kg
cost_of_oranges = price_of_oranges * quantity_of_oranges_kg
cost_of_bananas = price_of_bananas * quantity_of_bananas_kg
cost_of_raspberries = price_of_raspberries * quantity_of_raspberries_kg

total_sum = cost_of_bananas + cost_of_raspberries + cost_of_oranges + cost_of_strawberries
print (total_sum)
