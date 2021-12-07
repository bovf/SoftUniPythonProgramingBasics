price_of_holiday = float(input())
number_of_puzzles = int(input())
number_of_dolls = int(input())
number_of_bears = int(input())
number_of_minions = int(input())
number_of_trucks = int(input())

price_of_puzzles = 2.6
price_of_dolls = 3
price_of_bear = 4.1
price_of_minion = 8.2
price_of_truck = 2

money_from_puzzles = number_of_puzzles * price_of_puzzles
money_from_dolls = number_of_dolls * price_of_dolls
money_from_bears = number_of_bears * price_of_bear
money_from_minions = number_of_minions * price_of_minion
money_from_trucks = number_of_trucks * price_of_truck

total_money = money_from_bears + money_from_dolls + \
              money_from_minions + money_from_puzzles + \
              money_from_trucks
total_number_of_toys = number_of_bears + number_of_dolls + \
                       number_of_minions + number_of_puzzles + \
                       number_of_trucks

if total_number_of_toys >= 50:
    discount = total_money * 0.25
    rent = (total_money - discount) * 0.1
    profit = total_money - discount - rent
else:
    rent = total_money * 0.1
    profit = total_money - rent

if price_of_holiday <= profit:
    print(f"Yes! {profit - price_of_holiday:.2f} lv left.")
elif price_of_holiday > profit:
    print(f"Not enough money! {abs(profit - price_of_holiday):.2f} lv needed.")