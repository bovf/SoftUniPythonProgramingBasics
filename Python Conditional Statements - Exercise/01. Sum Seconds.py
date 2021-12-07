first_time = float(input())
second_time = float(input())
third_time = float(input())

sum_seconds = first_time + second_time + third_time
minutes = sum_seconds // 60
seconds_left = sum_seconds % 60

if seconds_left < 10:
    print(f"{minutes:.0f}:0{seconds_left:.0f}")
elif seconds_left >= 10:
    print(f"{minutes:.0f}:{seconds_left:.0f}")
