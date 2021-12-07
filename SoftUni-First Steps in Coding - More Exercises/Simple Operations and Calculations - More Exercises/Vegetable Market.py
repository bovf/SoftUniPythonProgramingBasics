price_of_vegetables_kg = float(input())
price_of_fruit_kg = float(input())
total_vegetables_kg = int(input())
total_fruits_kg = int(input())

total_price_vegetables = price_of_vegetables_kg * total_vegetables_kg
total_price_fruits = price_of_fruit_kg * total_fruits_kg
total_income_euro = (total_price_vegetables + total_price_fruits) / 1.94
print(f"{total_income_euro:.2f}")