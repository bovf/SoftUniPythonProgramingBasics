print("Question 1) Right now I would rather be :"
       "\n    A. Reading"
       "\n    B.Learning"
       "\n    C.Playing"
       "\n    D.Visiting")

total_points = 0


def question1():
    answer1 = input("Answer:")
    points = 0
    if answer1 == "A" or answer1 == "a":
        a1 = 2
        points = points + a1
    elif answer1 == "B" or answer1 == "b":
        a1 = 3
        points = points + a1
    elif answer1 == "C" or answer1 == "c":
        a1 = 4
        points = points + a1
    elif answer1 == "D" or answer1 == "d":
        a1 = 5
        points = points + a1
    else:
        print("Invalid input, try again.")
        points = question1()
    return points


points_question1 = int(question1())
total_points += points_question1
print(total_points)
