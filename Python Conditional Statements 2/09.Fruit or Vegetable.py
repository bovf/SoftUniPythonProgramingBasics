obj = str(input())
type_obj = str

if obj == "banana" or obj == "apple" or obj =="kiwi" or obj == "cherry" or obj == "lemon" or obj == "grapes":
    type_obj = "fruit"
elif obj == "tomato" or obj == "cucumber" or obj =="pepper" or obj == "carrot":
    type_obj = "vegetable"
else:
    type_obj = "unknown"

print(type_obj)