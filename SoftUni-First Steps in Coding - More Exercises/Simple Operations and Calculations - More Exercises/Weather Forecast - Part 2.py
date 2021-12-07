degrees = float(input())
state = str
# 26.00 - 35.00	Hot
# 20.1 - 25.9	Warm
# 15.00 - 20.00	Mild
# 12.00 - 14.9	Cool
# 5.00 - 11.9	Cold

if degrees >= 26 and degrees <= 35:
    state = "Hot"
elif degrees >= 20.1 and degrees <26:
    state = "Warm"
elif degrees >= 15 and degrees <= 20:
    state = "Mild"
elif degrees >= 12 and degrees <15:
    state = "Cool"
elif degrees >= 5 and degrees <12:
    state = "Cold"
elif degrees > 35 or degrees < 5:
    state = "unknown"

print(state)