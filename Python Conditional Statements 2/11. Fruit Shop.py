product = str(input())
day = str(input())
quantity = float(input())

price_banana = 0
price_apple = 0
price_orange = 0
price_grapefruit = 0
price_kiwi = 0
price_pineapple = 0
price_grapes = 0
price_general = 0
price_total = 0

if day == "Monday" or day == "Tuesday" or day == "Friday" or day == "Wednesday" or day == "Thursday":
    price_banana = 2.5
    price_apple = 1.2
    price_orange = 0.85
    price_grapefruit = 1.45
    price_kiwi = 2.7
    price_pineapple = 5.5
    price_grapes = 3.85
elif day == "Saturday" or day == "Sunday":
    price_banana = 2.7
    price_apple = 1.25
    price_orange = 0.9
    price_grapefruit = 1.6
    price_kiwi = 3
    price_pineapple = 5.6
    price_grapes = 4.2
if product == "banana":
    price_general = price_banana
elif product == "apple":
    price_general = price_apple
elif product == "orange":
    price_general = price_orange
elif product == "grapefruit":
    price_general = price_grapefruit
elif product == "kiwi":
    price_general = price_kiwi
elif product == "pineapple":
    price_general = price_pineapple
elif product == "grapes":
    price_general = price_grapes

price_total = price_general * quantity

if (product == "apple" or product == "orange" or
    product == "grapefruit" or product == "kiwi" or
    product == "pineapple" or product == "grapes"
    or product == "banana")\
        and (day == "Monday" or day == "Tuesday" or
             day == "Friday" or day == "Wednesday" or
             day == "Thursday" or day == "Saturday" or
             day == "Sunday"):
        print (f"{price_total:.2f}")
else:
    print("error")
