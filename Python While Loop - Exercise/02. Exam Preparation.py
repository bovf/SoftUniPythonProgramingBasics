max_failing_grades = int(input())

failing_grade_counter = 0
problem_counter = 0
last_problem = str
grade_sum = 0
while True:
    entry = str(input())
    if entry == "Enough":
        print(f"Average score: {(grade_sum/problem_counter):.2f}"
              f"\nNumber of problems: {problem_counter}"
              f"\nLast problem: {last_problem}")
        break
    last_problem = entry
    grade = int(input())
    grade_sum += grade
    if grade <= 4:
        failing_grade_counter += 1
    problem_counter += 1
    if failing_grade_counter >= max_failing_grades:
        print(f"You need a break, {max_failing_grades} poor grades.")
        break
