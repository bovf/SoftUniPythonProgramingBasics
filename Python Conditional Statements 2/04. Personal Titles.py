age = float(input())
gender = str(input())

# •	"Mr." – мъж (пол 'm') на 16 или повече години
# •	"Master" – момче (пол 'm') под 16 години
# •	"Ms." – жена (пол 'f') на 16 или повече години
# •	"Miss" – момиче (пол 'f') под 16 години

if gender == "m":
    if age < 16:
        print("Master")
    else:
        print("Mr.")
else:
    if age < 16:
        print("Miss")
    else:
        print("Ms.")
