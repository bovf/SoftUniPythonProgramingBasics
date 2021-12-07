import math

monthly_salary = float(input())
median_grade = float(input())
minimum_wage = float(input())

# social_scholarship = 0.35 * minimum_wage
# social_scholarship only defined if scholarship_for_excellency_condition is true
# excellency_scholarship = median_grade * 25
# excellency_scholarship only defined if scholarship_for_excellency_condition is true
scholarship_for_excellency_condition = bool
scholarship_for_social_purposes_condition = bool
scholarship = 0

# if block checks if the candidate eligible for a social scholarship
if monthly_salary < minimum_wage and median_grade > 4.5:
    scholarship_for_social_purposes_condition = True
    social_scholarship = 0.35 * minimum_wage
else:
    scholarship_for_social_purposes_condition = False
# if block checks if the candidate eligible for a social excellency scholarship
if median_grade >= 5.5:
    scholarship_for_excellency_condition = True
    excellency_scholarship = median_grade * 25
else:
    scholarship_for_excellency_condition = False

# if block printing the result depending on the eligibility of the candidates
if scholarship_for_excellency_condition == True and scholarship_for_social_purposes_condition == False:
    scholarship = excellency_scholarship
    print(f"You get a scholarship for excellent results {math.floor (scholarship)} BGN")
elif scholarship_for_excellency_condition == False and scholarship_for_social_purposes_condition == True:
    scholarship = social_scholarship
    print(f"You get a Social scholarship {math.floor (scholarship)} BGN")
elif scholarship_for_excellency_condition == True and scholarship_for_social_purposes_condition == True:
    # if block getting the higher scholarship amount
    if excellency_scholarship > social_scholarship:
        scholarship = excellency_scholarship
    elif social_scholarship > excellency_scholarship:
        scholarship = social_scholarship
    elif social_scholarship == excellency_scholarship:
        scholarship = excellency_scholarship
    # if block printing the right message depending on the scholarship amount
    if excellency_scholarship >= social_scholarship:
        print(f"You get a scholarship for excellent results {math.floor (scholarship)} BGN")
    else:
        print(f"You get a Social scholarship {math.floor (scholarship)} BGN")
else:
    print("You cannot get a scholarship!")
