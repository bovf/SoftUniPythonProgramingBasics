screening_type = str(input())
rows = int(input())
columns = int(input())

total_seats = rows * columns
price_per_seat = float

if screening_type == "Premiere":
    price_per_seat = 12
elif screening_type == "Normal":
    price_per_seat = 7.5
elif screening_type == "Discount":
    price_per_seat = 5

total_cost = price_per_seat * total_seats

print(f"{total_seats:.2f} leva")