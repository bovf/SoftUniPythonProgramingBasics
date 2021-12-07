length_cm = int(input())
width_cm = int(input())
height_cm = int(input())
percentage_оccupied = float(input())

cubic_liters_of_aquarium = length_cm * width_cm * height_cm * 0.001
cubic_liters_of_water =cubic_liters_of_aquarium - cubic_liters_of_aquarium * percentage_оccupied * 0.01

print(cubic_liters_of_water)

