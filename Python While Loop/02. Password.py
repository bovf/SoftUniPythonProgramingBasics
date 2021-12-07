name = str(input())
password = str(input())
password_input = str

while password_input != password:
    password_input = str(input())
print(f"Welcome {name}!")
