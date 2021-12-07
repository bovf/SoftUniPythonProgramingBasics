number = float(input())
metric_input = str(input())
metric_output = str(input())
number_in_millimeters = 0
if metric_input == "m":
    number_in_millimeters = number * 1000
elif metric_input == "mm":
    number_in_millimeters = number
elif metric_input == "cm":
    number_in_millimeters = number * 10

if metric_output == "mm":
    print(f"{number_in_millimeters:.3f}")
elif metric_output == "cm":
    print(f"{number_in_millimeters / 10:.3f}")
elif metric_output == "m":
    print(f"{number_in_millimeters / 1000:.3f}")
