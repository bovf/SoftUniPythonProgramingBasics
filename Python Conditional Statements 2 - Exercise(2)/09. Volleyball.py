from math import floor
year_type = str(input())
p = int(input())
h = int(input())

weekends = 48
saturdays_playing = 3 / 4 * (weekends - h)
sundays_playing = h
holidays_playing = p * 2 / 3
total_days_playing = saturdays_playing + sundays_playing + holidays_playing

total_days_playing_leap = 0
total_days_playing_normal = 0

if year_type == "leap":
    total_days_playing_leap = total_days_playing + (total_days_playing * 0.15)
    print(f"{(floor(total_days_playing_leap))}")
elif year_type == "normal":
    total_days_playing_normal = total_days_playing
    print(f"{(floor(total_days_playing_normal))}")
