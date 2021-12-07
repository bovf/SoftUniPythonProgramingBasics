n = int(input())
salary = float(input())

facebook_fine = 150
instagram_fine = 100
reddit_fine = 50

fines = 0
for a in range(0, n):
    site_name = str(input())
    if site_name == "Facebook":
        fines += facebook_fine
    if site_name == "Reddit":
        fines += reddit_fine
    if site_name == "Instagram":
        fines += instagram_fine
    if fines >= salary:
        print (f"You have lost your salary.")
        break

final_salary = salary - fines

if final_salary > 0:
    print(f"{final_salary:.0f}")
