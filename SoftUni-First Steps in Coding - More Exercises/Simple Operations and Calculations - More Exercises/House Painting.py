x = float(input())
y = float(input())
h = float(input())

door = 1.2 * 2
window = 1.5 * 1.5

walls_m2 = (x * x) * 2 + (y * x) * 2 - door - (2 * window)
roof = (x * h / 2) * 2 + (x * y) * 2
green_paint = walls_m2 / 3.4
red_paint = roof / 4.3

print(f"{green_paint:.2f}")
print(f"{red_paint:.2f}")