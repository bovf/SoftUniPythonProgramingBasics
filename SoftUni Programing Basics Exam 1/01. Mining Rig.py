import math

price_graphics_card = int(input())
price_adapter = int(input())
price_electricity_day_card = float(input())
profit_day_card = float(input())

total_price_graphics = price_graphics_card * 13
total_price_adapter = price_adapter * 13
total_price_misc = 1000
total_spent = total_price_misc + total_price_adapter + total_price_graphics

pure_profit_card = profit_day_card - price_electricity_day_card
total_profit_day = pure_profit_card * 13
days_till_profit = math.ceil(total_spent / total_profit_day)

print(f"{total_spent}")
print(f"{days_till_profit}")
