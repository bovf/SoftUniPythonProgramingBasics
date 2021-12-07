obj = str(input())

type_obj = str
fruits = ["banana", "apple", "kiwi", "cherry", "lemon", "grapes"]
vegetables = ["tomato", "cucumber", "pepper", "carrot"]
counter_f = 0
counter_v = 0

for a in fruits:
    if a != obj:
        print(counter_f)
        counter_f += 1
    else:
        type_obj = "fruit"
for a in vegetables:
    if a != obj:
        counter_v += 1
    else:
        type_obj = "vegetable"
if counter_f == 6 and counter_v == 4:
    type_obj = "unknown"

print(type_obj)
print(counter_f)