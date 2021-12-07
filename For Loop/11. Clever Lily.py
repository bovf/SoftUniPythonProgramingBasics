# •	Възрастта на Лили - цяло число в интервала [1...77]
# •	Цената на пералнята - число в интервала [1.00...10 000.00]
# •	Единична цена на играчка - цяло число в интервала [0...40]
age = int(input())
price_washing_machine = float(input())
price_toy = int(input())

money_present = 0
money_counter = 0
money_toys = 0
brother_stolen_money = 0
for a in range(1, age + 1):
    if a % 2 == 0:
        money_counter += 1
        for i in range(0, money_counter):
            money_present += 10
    else:
        money_toys += price_toy

brother_stolen_money = money_counter
money_total = money_present + money_toys - brother_stolen_money
money_left = money_total - price_washing_machine

if money_total >= price_washing_machine:
    print(f"Yes! {money_left:.2f}")
else:
    print(f"No! {abs(money_left):.2f}")