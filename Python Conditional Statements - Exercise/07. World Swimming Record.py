current_record = float(input())
distance_m = float(input())
time_per_meter = float(input())

time_needed = time_per_meter * distance_m
time_total = distance_m // 15 * 12.5 + time_needed

if time_total >= current_record:
    print(f"No, he failed! He was {abs(current_record - time_total):.2f} seconds slower.")
elif time_total < current_record:
    print(f"Yes, he succeeded! The new world record is {time_total:.2f} seconds.")