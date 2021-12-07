import math

monthly_salary = float(input())
median_grade = float(input())
minimum_wage = float(input())

social_scholarship = 0.35 * minimum_wage
excellency_scholarship = median_grade * 25
scholarship_for_excellency_condition = str
scholarship_for_social_purposes_condition = str
scholarship = 0


if monthly_salary < minimum_wage and median_grade > 4.5:
    scholarship_for_social_purposes_condition = "True"
else:
    scholarship_for_social_purposes_condition = "False"
if median_grade >= 5.5:
    scholarship_for_excellency_condition = "True"
else:
    scholarship_for_excellency_condition = "False"

if scholarship_for_excellency_condition == "True" and scholarship_for_social_purposes_condition == "True":
    if excellency_scholarship > social_scholarship:
        scholarship = excellency_scholarship
    elif social_scholarship > excellency_scholarship:
        scholarship = social_scholarship
    elif social_scholarship == excellency_scholarship:
        scholarship = excellency_scholarship
elif scholarship_for_social_purposes_condition == "True":
    scholarship = social_scholarship
elif scholarship_for_excellency_condition == "True":
    scholarship = excellency_scholarship

if scholarship_for_excellency_condition == "False" and scholarship_for_social_purposes_condition == "False":
    print("You cannot get a scholarship!")
elif scholarship_for_excellency_condition == "True" and scholarship_for_social_purposes_condition == "False":
    print(f"You get a scholarship for excellent results {math.floor(scholarship)} BGN")
elif scholarship_for_excellency_condition == "False" and scholarship_for_social_purposes_condition == "True":
    print(f"You get a Social scholarship {math.floor(scholarship)} BGN")
elif scholarship_for_excellency_condition == "True" and scholarship_for_social_purposes_condition == "True":
    if excellency_scholarship >= social_scholarship:
        print(f"You get a scholarship for excellent results {math.floor(scholarship)} BGN")
    else:
        print(f"You get a Social scholarship {math.floor(scholarship)} BGN")
