steps_goal = 10000
steps_sum = 0
failed = False

while steps_sum < steps_goal:
    steps_entry = input()
    if steps_entry == "Going home":
        steps_to_home = int(input())
        steps_sum += steps_to_home
        if steps_sum < steps_goal:
            failed = True
        break
    else:
        steps_sum += int(steps_entry)

if failed:
    print(f"{(abs(steps_goal - steps_sum))} more steps to reach goal.")
else:
    print(f"Goal reached! Good job!"
          f"\n{(abs(steps_goal - steps_sum))} steps over the goal!")
