time_input_hours = int(input())
time_input_minutes = int(input())

total_time_minutes = time_input_hours * 60 + time_input_minutes
new_time = total_time_minutes + 15

new_time_hours = new_time // 60
new_time_minutes = new_time % 60
if new_time_hours >= 24:
    new_time_hours = 0

if new_time_minutes < 10:
    print(f"{new_time_hours:.0f}:0{new_time_minutes:.0f}")
elif new_time_minutes >= 10:
    print(f"{new_time_hours:.0f}:{new_time_minutes:.0f}")
