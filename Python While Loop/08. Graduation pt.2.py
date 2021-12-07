name = str(input())

failing_grades_counter = 0
passing_grade_counter = 0
passing_grade_sum = 0
total_grade_counter = 0
total_grade_sum = 0
while True:
    if failing_grades_counter >= 2:
        print(f"{name} has been excluded at {(total_grade_counter - 1)} grade")
        break
    if passing_grade_counter == 12:
        print(f"{name} graduated. "
               f"Average grade: {(passing_grade_sum / passing_grade_counter):.2f}")
        break
    grade = float(input())
    if grade < 4:
        failing_grades_counter += 1
    else:
        passing_grade_counter += 1
        passing_grade_sum += grade
    total_grade_sum += grade
    total_grade_counter += 1
