stay_days = int(input())
room_type = str(input())
rating = str(input())

discount = 0
price_day = 0
total_cost = 0
final_cost = 0

stay_nights = int(stay_days - 1)

if room_type == "room for one person":
    price_day = 18
elif room_type == "apartment":
    price_day = 25
elif room_type == "president apartment":
    price_day = 35

total_cost = stay_nights * price_day

if stay_nights < 10:
    if room_type == "room for one person":
        discount = 0
        final_cost = total_cost
    elif room_type == "apartment":
        discount = 0.3
        final_cost = total_cost - total_cost * discount
    elif room_type == "president apartment":
        discount = 0.1
        final_cost = total_cost - total_cost * discount
elif 10 <= stay_nights <= 15:
    if room_type == "room for one person":
        discount = 0
        final_cost = total_cost
    elif room_type == "apartment":
        discount = 0.35
        final_cost = total_cost - total_cost * discount
    elif room_type == "president apartment":
        discount = 0.15
        final_cost = total_cost - total_cost * discount
elif stay_nights > 15:
    if room_type == "room for one person":
        discount = 0
        final_cost = total_cost
    elif room_type == "apartment":
        discount = 0.5
        final_cost = total_cost - total_cost * discount
    elif room_type == "president apartment":
        discount = 0.2
        final_cost = total_cost - total_cost * discount

if rating == "positive":
    print(f"{final_cost + final_cost * 0.25:.2f}")
else:
    print(f"{final_cost - final_cost * 0.1:.2f}")
