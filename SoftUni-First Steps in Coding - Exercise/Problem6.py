days_of_campaign = int(input())
number_of_bakers = int(input())
number_of_cakes = int(input())
number_of_waffles = int(input())
number_of_pancakes = int(input())

cost_of_cake = float(45)
cost_of_waffle = float(5.80)
cost_of_pancake = float(3.20)
money_from_cakes = number_of_cakes * cost_of_cake
money_from_waffles = number_of_waffles * cost_of_waffle
money_from_pancakes =  number_of_pancakes * cost_of_pancake

money_per_day = (money_from_waffles + money_from_pancakes + money_from_cakes) * number_of_bakers
sum_of_money_collected = money_per_day * days_of_campaign
cost_of_campaign = sum_of_money_collected / 8
total_money_collected = sum_of_money_collected - cost_of_campaign

print(round (total_money_collected, 2))
