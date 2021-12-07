import math

sex = str(input())
weight_kg = float(input())
height = float(input())
age = int(input())
activity_level = str(input())

bnm = 0
height_cm = height * 100
if sex == "m":
    bnm = 66 + (13.7 * weight_kg) + (5 * height_cm) - (6.8 * age)
else:
    bnm = 655 + (9.6 * weight_kg) + (1.8 * height_cm) - (4.7 * age)

if activity_level == "sedentary":
    k = 1.2
elif activity_level == "lightly active":
    k = 1.375
elif activity_level == "moderately active":
    k = 1.55
elif activity_level == "very active":
    k = 1.725

calories_day = math.ceil(bnm * k)

print(f"To maintain your current weight you will need {calories_day} calories per day.")