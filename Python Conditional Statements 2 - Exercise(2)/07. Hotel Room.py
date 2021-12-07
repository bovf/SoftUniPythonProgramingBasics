month = str(input())
nights = int(input())

months_list = ["May", "June", "July", "August", "September", "October"]
months_counter = 0
for a in months_list:
    if a == month:
        break
    else:
        months_counter += 1

studio_per_night = 0
apartment_per_night = 0

if months_counter == 0 or months_counter == 5:
    studio_per_night = 50
    apartment_per_night = 65
elif months_counter == 1 or months_counter == 4:
    studio_per_night = 75.2
    apartment_per_night = 68.7
elif months_counter == 2 or months_counter == 3:
    studio_per_night = 76
    apartment_per_night = 77

cost_for_studio = 0
cost_for_apartment = 0
discount_studio = 0
discount_apartment = 0

if 13 >= nights > 7 and (months_counter == 0 or months_counter == 5):
    discount_studio = 0.05
    cost_for_studio = (nights * studio_per_night) - (nights * studio_per_night * discount_studio)
elif nights > 14 and (months_counter == 0 or months_counter == 5):
    discount_studio = 0.3
    cost_for_studio = (nights * studio_per_night) - (nights * studio_per_night * discount_studio)
elif nights > 14 and (months_counter == 1 or months_counter == 4):
    discount_studio = 0.2
    cost_for_studio = (nights * studio_per_night) - (nights * studio_per_night * discount_studio)
else:
    cost_for_studio = nights * studio_per_night

if nights > 14:
    discount_apartment = 0.1
    cost_for_apartment = (nights * apartment_per_night) - (nights * apartment_per_night * discount_apartment)
else:
    cost_for_apartment = nights * apartment_per_night

print(f"Apartment: {cost_for_apartment:.2f} lv.")
print(f"Studio: {cost_for_studio:.2f} lv.")